from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
