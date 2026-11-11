from openai import OpenAI

MODEL = "gpt-6-luna"    

client = OpenAI()        

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Say Good Morning in one sentence with  a gree in polite way with question."},
    ],
)

print(response.choices[0].message.content)