from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
