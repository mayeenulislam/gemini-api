# Put image as an Input to the Gemini LLM

import os
import google.generativeai as genai

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')


# Image as an Input:
# --------------------------------

import PIL

image = PIL.Image.open('assets/sample-image.jpg')
# vision_model = genai.GenerativeModel('gemini-pro-vision') # deprecated since 12 July 2024
vision_model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Explain the image
response = vision_model.generate_content(["Explain the picture", image])

# Generate a story based on the image
# response = vision_model.generate_content(["Write a story from the picture and set a title with suspected place where the image was taken", image])

# Count the objects from the image and response in JSON format
# response = vision_model.generate_content(["Generate a json of ingredients with their count visible in the image", image])

print(response.text)
