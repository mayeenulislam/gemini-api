# Chat with Gemini LLM

import os
import google.generativeai as genai

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')


# Chat Vision of Gemini LLM:
#
# Difference is to use `GenerativeModel.start_chat()` function
# instead of `GenerativeModel.generate_text()`
# --------------------------------

chat = model.start_chat(history = []) # empty list is provided on initiation

response = chat.send_message("What are the outer planets in the Solar System?")
print(response.text)

response = chat.send_message("Write down the colors of them")
print(response.text)

print(chat.history)

# Footnote:
# Google offers the option to establish a chat with existing history
