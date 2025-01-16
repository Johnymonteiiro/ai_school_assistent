from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
