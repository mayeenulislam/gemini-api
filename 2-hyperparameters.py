# Learning Hyperparameters of Gemini LLM

import os
import google.generativeai as genai

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')


# Setting Hyperparameters:
# --------------------------------

response = model.generate_content(
    "What is Quantum Computing?",
    generation_config = genai.types.GenerationConfig(
        # Directs the Gemini to generate only a single response per Prompt/Query
        candidate_count = 1,

        # Instructs Gemini to conclude text generation upon encountering a period (.) in the content
        stop_sequences = ['.'],

        # Imposes a constraint on the generated text,
        # limiting it to a specified maximum length,
        # set here to 40 tokens
        max_output_tokens = 40,

        # Influences the likelihood of selecting the next
        # best word based on its probability.
        # A value of 0.6 emphasizes more probable words,
        # while higher values lean towards less likely
        # but potentially more creative choices
        top_p = 0.6,

        # Takes into consideration only the top 5 most
        # likely words when determining the next word,
        # fostering diversity in the output
        top_k = 5,

        # Governs the randomness of the generated text.
        # A higher temperature, such as 0.8, elevates randomness and creativity,
        # while lower values lean towards more predictable and conservative outputs
        temperature = 0.8
    )
)

print(response.text)
