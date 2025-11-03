from openai import OpenAI
client = OpenAI(api_key="...")
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "hello world"}],
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "")