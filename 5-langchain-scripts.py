# Langchain
# The file name is `langchain_scripts.py` instead of `langchain.py` to prevent
# 'circular import issue' as it shadows the actual `langchain` library

import os
import google.generativeai as genai

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


# Integrating Langchain with Gemini:
# --------------------------------
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Single input
# llm.invoke()
# response = llm.invoke("Sing a ballad of LangChain.")

# print(response.content)

# Multiple inputs with batch responses
# llm.batch()
batch_responses = llm.batch([
    # Will get an answer for this open question
    "Where is Olympus Mons located?",

    # Won't get answer because this one is not chained with the previous question
    # 👉 It's just an individual question
    "What its height?",
])

for response in batch_responses:
    print(response.content)
