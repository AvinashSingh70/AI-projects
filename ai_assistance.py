from openai import OpenAI
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv()

#create an Client that communicates with the ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("*" *40)
print("  My AI Assistant  ")
print("*" *40)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the AI Assistant. Goodbye!")
        break

    #Send a question to the AI model
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    #retrieve and print the AI's response
    print("AI: " + response.choices[0].message.content)

