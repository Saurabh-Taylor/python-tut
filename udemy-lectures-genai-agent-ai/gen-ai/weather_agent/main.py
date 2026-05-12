from openai import OpenAI
from dotenv import load_dotenv
from agent import SYSTEM_PROMPT
load_dotenv()


client = OpenAI()

def main():
    
    user_query = input(">")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"system",
                "content": SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content": user_query
            }
        ]
    )

    print(f"Response: {response.choices[0].message.content}")

main()