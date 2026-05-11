from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

client = OpenAI()

# few-shot prompting  => Directly giving instructions to the model and few examples to the model.
SYSTEM_PROMPT = """
You Should only and only ans the coding related questions. Do not ans anything else. Your Name is Saturday. If User asks something other than coding, just say sorry

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
"code": "string" or null,
"isCodingQuestion": boolean
}}

Examples:
Q. Can You Explain the a + b whole square?
A. {{ "code": null,"isCodingQuestion": false }}

Q. Write a code in python for adding two number?
A. {{ "code": "def add(a, b):
    return a + b",
    "isCodingQuestion": false 
    }}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"system",
            "content": SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content": "Can You Explain the a + b whole square?"
        }
    ]
)

print(response.choices[0].message.content)