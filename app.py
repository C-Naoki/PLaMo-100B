import csv
import datetime
import io
import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    base_url=f"{os.environ['API_HOST']}/api/completion/v1",
    api_key=os.environ["API_KEY"],
)

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Streamlit app
st.title("汎用チャットボット")

# System message input
system_message = st.text_area("システムメッセージを入力してください：", "あなたは役立つアシスタントです。")

# User input
user_input = st.text_area("メッセージを入力してください：", "こんにちは、今日の天気はどうですか？")

if st.button("応答を取得"):
    # Create a placeholder for the output
    output_placeholder = st.empty()

    # Prepare messages for API call
    api_messages = [
        {"role": "system", "content": system_message},
        *[msg for conv in st.session_state.conversation for msg in conv['messages']]
    ]
    api_messages.append({"role": "user", "content": user_input})

    # Call the API
    completion = client.chat.completions.create(
        model="plamo-beta",
        messages=api_messages,
        stream=True,
    )

    full_response = ""

    # Stream the response
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            # Update the placeholder with the accumulated response
            output_placeholder.markdown(full_response)

    # Add the new conversation pair to the history with timestamp
    st.session_state.conversation.append({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": full_response}
        ]
    })

# Display conversation history with toggle and message limit
show_history = st.toggle("会話履歴を表示", value=True)

if show_history and st.session_state.conversation:
    st.subheader("会話履歴")

    # Input for the number of recent messages to display
    num_messages = st.number_input(
        "表示する最近のメッセージ数",
        min_value=1,
        max_value=len(st.session_state.conversation),
        value=min(5, len(st.session_state.conversation))
    )

    # Display selected number of recent messages in reverse order
    for conv in reversed(st.session_state.conversation[-num_messages:]):
        st.markdown("---")
        st.markdown(f"{conv['timestamp']}")
        st.markdown(f"**Q.** {conv['messages'][0]['content']}")
        st.markdown(f"**A.** {conv['messages'][1]['content']}")
    st.markdown("---")

    # CSV export function
    def export_to_csv():
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Timestamp", "User", "Assistant"])
        for conv in reversed(st.session_state.conversation):
            writer.writerow([
                conv['timestamp'],
                conv['messages'][0]['content'],
                conv['messages'][1]['content']
            ])
        return output.getvalue()

    # CSV export button (now directly triggers download)
    csv_data = export_to_csv()
    st.download_button(
        label="会話履歴をCSVでエクスポート",
        data=csv_data,
        file_name="chat_history.csv",
        mime="text/csv"
    )

elif show_history:
    st.info("まだ会話履歴がありません。チャットを開始してください。")

st.markdown("---")
st.markdown("""
このウェブアプリに関する詳細は、以下の記事及びソースコードをご覧ください。

- [PLaMo-100Bのβ版トライアルAPIを用いてデモ用アプリを作ってみた](https://zenn.dev/naoki0103/articles/plamo100b-demo)
- [ソースコード](https://github.com/C-Naoki/PLaMo-100B)
""")
