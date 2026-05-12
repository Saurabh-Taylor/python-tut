
import requests
from pydantic import BaseModel, Field


class MyOutputFormat(BaseModel):
   step: str = Field(..., description="This can be START, PLAN, OUTPUT or TOOL") 

def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    
    return f"Could not retrieve weather data for {city}."

# chain of thought prompting
SYSTEM_PROMPT = """
    You're an Expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. the PLAN can be multiple steps.
    Once You Think Enough PLAN has been done, finally you can give an output.
    You can also use tool if required from the list of available tools.


    Rules:
    - Strictly Follow the given JSON output format
    - Only Run one step at a time.
    - The Sequence of steps is START(where user gives an input), PLAN(That can be multiple times) and finally OUTPUT(which is goin to be displayed to the user).

    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": string }

    Available Tools:
    - get_weather(city: str) -> str : Takes city name as input and gives the current weather information of the city.

    Example 1:
    START: Hey Can You Solve 2 + 3 * 5 /10
    PLAN: {"step": "PLAN", "content":"Seems like user is interested in math problem"}
    PLAN: {"step": "PLAN", "content":"looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN", "content":"Yes the BODMAS is correct thing to be done here"}
    PLAN: {"step": "PLAN", "content":"First we must multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN", "content":"Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN", "content":"We must perform the divide that is 15 / 10 = 1.5"}
    PLAN: {"step": "PLAN", "content":"Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content":"Now finally lets perform the add"}
    PLAN: {"step": "PLAN", "content":"Great we have solved and finally left with 1.5 as ans"}
    OUTPUT: {"step": "OUTPUT", "content":"3.5"}

    Example 2:
    START: What is the weather in Delhi?
    PLAN: {"step": "PLAN", "content":"User wants to know the weather in Delhi"}
    PLAN: {"step": "PLAN", "content":"To know the weather we can use the get_weather tool that is available to us"}
    PLAN: {"step": "PLAN", "content":"We can call the tool like this get_weather(city='Delhi')"}
    PLAN: {"step": "PLAN", "content":"Yes that seems correct, we can call the tool now to get the weather information"}
    TOOL: {"step": "TOOL", "content":"get_weather(city='Delhi')"}
    OUTPUT: {"step": "OUTPUT", "content":"The weather in Delhi is: Partly cloudy, 22°C"}

"""

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role":"system",
#             "content": SYSTEM_PROMPT
#         },
#         {
#             "role":"user",
#             "content": "Hey write a code to add n numbers in js"
#         }
#     ]
# )

# print(response.choices[0].message.content)