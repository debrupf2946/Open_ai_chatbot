import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key=os.getenv('OPENAI_API_KEY')
message_history=[]

while True:
    user_input=input(">:")
    print("user input was:",user_input)
    message_history.append({"role":"user","content":user_input})
    if user_input=="end":
        break
    else:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
        )

        completion_1=completion.choices[0].message.content
        print(completion_1)

