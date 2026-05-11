from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

client = OpenAI()

# zero-shot prompting  => Directly giving instructions to the model, the model is given a direct question or task without prior examples.
SYSTEM_PROMPT = "You are a helpful assistant that helps user to maths related problems only"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"system",
            "content": SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content": "can u tell me a joke"
        }
    ]
)

print(response.choices[0].message.content)