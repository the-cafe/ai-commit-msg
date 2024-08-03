from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

class OpenAiService:
    def __init__(self):
      api_key = "sk-proj-pPkf0GH5LzbVFno8Eyc1T3BlbkFJY628EJOBgGN6wNMN494j"

      if(api_key is None):
        raise Exception("OPENAI_API_KEY is not set")
      self.client = OpenAI(api_key="sk-proj-pPkf0GH5LzbVFno8Eyc1T3BlbkFJY628EJOBgGN6wNMN494j")

    def chat_with_openai(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return completion.choices[0].message.content
