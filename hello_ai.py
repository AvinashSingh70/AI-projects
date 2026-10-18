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

#Send a question to the AI model
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

#retrieve and print the AI's response
print(response.choices[0].message.content)