import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url=f"{os.environ['API_HOST']}/api/completion/v1",
    api_key=os.environ["API_KEY"],
)

completion = client.chat.completions.create(
    model="plamo-beta",
    messages=[
        {"role": "system", "content": "あなたは旅行アドバイザーです"},
        {"role": "user", "content": "金沢で朝から夕方まで1日のおすすめの観光ルートを教えて下さい"},
    ],
    stream=True,
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
