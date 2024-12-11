from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = ""
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
