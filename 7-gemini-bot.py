# Gemini Bot: Creating a GUI using Streamlit

import streamlit as st
import os
import google.generativeai as genai

st.title("Gemini Bot")

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

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
