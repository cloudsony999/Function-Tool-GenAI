from dotenv import load_dotenv
from google import genai
from google.genai import types
import os


key = os.getenv("GOOGLE_API_KEY")
load_dotenv()
client= genai.Client(api_key=key)


def add_numbers (a: float, b: float) -> float:
    return a+b

def course_info (topic: str) -> str:
    courses={
    "python": "Python basics, control flow, functions",
    "rag": "Load, split, embed, retrieve, ground answers",
    "agents": "LLM decisions, tools, state, evaluation"
    }
    return courses.get(topic.lower().strip(), "No course found.")



chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        tools=[add_numbers, course_info],
        temperature=0
    )
)

# Send the message through the chat session
response = chat.send_message("Calculate 25 plus 17 and explain a RAG course.")
print (response.text)
