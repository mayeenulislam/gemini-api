# Gemini Bot: Creating a GUI using Streamlit
# NO SAFETY IS CHECKED

import streamlit as st
import os
import google.generativeai as genai

st.title("Gemini Bot")

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# Set up the model
generation_config = {
    "max_output_tokens": 2048,
    "top_p": 1,
    "top_k": 1,
    "temperature": 0.9,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

model = genai.GenerativeModel(
    model_name = 'gemini-pro',
    generation_config = generation_config,
    safety_settings = safety_settings
)



# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me anything...",
        }
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Process and store query and response
def llm_function(query):
    response = model.generate_content(query)

    # Displaying the Assistant Message
    with st.chat_message("assistant"):
          st.markdown(response.text)
    
    # Storing the User Message
    st.session_state.messages.append(
         {
              "role": "user",
              "content": query,
         }
    )

    # Storing the Replied Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text,
        }
    )

# Accept user Input
# chat_input()
query = st.chat_input("What's up?")

# Calling the function when the Input is Provided
if query:
    # Display the user message
    with st.chat_message("user"):
         st.markdown(query)

    llm_function(query)
