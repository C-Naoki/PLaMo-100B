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
st.title("PLaMo-100B Chat Demo")

# System message input
system_message = st.text_area("Please enter a system message:", "You are a professional translator of Japanese and English.")

# User input
user_input = st.text_area("Please enter a message to PLaMo-100B:", "Please translate the following English sentence into Japanese: 'One of my favorite mangas is One Piece.'")

if st.button("get response"):
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
show_history = st.toggle("display conversation history", value=True)

if show_history and st.session_state.conversation:
    st.subheader("Conversation history")

    # Input for the number of recent messages to display
    num_messages = st.number_input(
        "number of recent messages to display",
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
        label="export conversation history to CSV",
        data=csv_data,
        file_name="chat_history.csv",
        mime="text/csv"
    )

elif show_history:
    st.info("No conversation history available. Let's send a message!")

st.markdown("---")
st.markdown("""
Please refer to the following articles and source code for details about this web application.

- [PLaMo-100Bのβ版トライアルAPIを用いてデモ用アプリを作ってみた](https://zenn.dev/naoki0103/articles/plamo100b-demo)
- [Source code (github)](https://github.com/C-Naoki/PLaMo-100B)
""")
