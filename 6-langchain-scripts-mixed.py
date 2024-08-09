# Langchain: Mixed
# Both textual and image as an input

import os
import google.generativeai as genai

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

from langchain_google_genai import ChatGoogleGenerativeAI


# Using both text and images with LangChain:
# --------------------------------
from langchain_core.messages import HumanMessage

# llm = ChatGoogleGenerativeAI(model="gemini-pro-vision") # deprecated since 12 July 2024
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Interacting with a single image and a single text
message = HumanMessage(
    content = [
        {
            "type": "text",
            "text": "Describe the image",
        },
        {
            "type": "image_url",
            "image_url": 'assets/sample-image.jpg', # could be remote URL of an image as well
        },
    ]
)

# Find differences between two given images
# message = HumanMessage(
#     content=[
#         {
#             "type": "text",
#             "text": "Find the differences between the given images",
#         },
#         {
#             "type": "image_url",
#             "image_url": "https://picsum.photos/id/237/200/300"
#         },
#         {
#             "type": "image_url",
#             "image_url": "https://picsum.photos/id/219/5000/3333"
#         }
#     ]
# )

response = llm.invoke([message])

print(response.content)
