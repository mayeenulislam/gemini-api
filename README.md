# Gemini Bot

## Gemini API Pricing

As of 2024-05-29 | 16:24 | Gemini 1.5 Flash

- 15 RPM (requests per minute)
- 1 million TPM (tokens per minute)
- 1,500 RPD (requests per day)
- Input: Free
- Output: Free

https://ai.google.dev/pricing

## Prerequisites

0. Python environment
1. Gemini API Key from https://makersuite.google.com
2. Python virtual environment

```bash
python -m venv venv

#for ubuntu
source venv/bin/activate

#for windows
venv/Scripts/activate
```

## How to use

```bash
git clone https://github.com/mayeenulislam/gemini-api && \
    cd gemini-api
```

### Install the Requirements

#### Install the Frozen Versions

```bash
pip install -r requirements.txt
```

#### Or, Install Manually

Or, Install the Latest Versions

```bash
pip install google-generativeai langchain-google-genai streamlit pillow
```

### Get and Set the API Key

```bash
export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

> On Windows this will create an Environment variable to the OS, but on Linux and Mac this will set the environment variable for the shell session

Gemini API Key from <https://makersuite.google.com><br/>
and Set it on `.env` file

## Files and their tasks

```bash
python <FILENAME>.py
```

1. `1-app.py`: Testing the API key and Hello World
2. `2-hyperparameters.py`: The configuration that could be used
3. `3-image-input.py`: Working with image as an input
4. `4-chat.py`: Working with Chat mode of Gemini LLM
5. `5-langchain-scripts.py`: Using LangChain using `ChatGoogleGenerativeAI` class (file name has a lesson learnt)
6. `6-langchain-scripts-mixed.py`: Using LangChain to mix textual and image inputs (both)

```bash
streamlit run gemini-bot.py
```

7. `7-gemini-bot.py`: Creating a GUI using Streamlit
8. `8-gemini-bot-safety-0.py`: Using the `generation_config` to set Safety Parameters

### `4-chat.py`

History response example:

```python
[
    parts {
        text: "What are the outer planets in the Solar System?"
    }
    role: "user",
    
    parts {
        text: "* Jupiter\n* Saturn\n* Uranus\n* Neptune"
    }
    role: "model",
    
    parts {
        text: "Write down the colors of them"
    }
    role: "user",
    
    parts {
        text: "* **Jupiter:** Brownish-orange with white, red, brown, and yellow clouds\n* **Saturn:** Pale yellow with golden bands and a bluish tint\n* **Uranus:** Pale blue-green\n* **Neptune:** Deep blue\n\nThe colors of the outer planets are caused by the absorption and scattering of sunlight by gases and particles in their atmospheres. Jupiter\'s atmosphere is mostly composed of hydrogen and helium, with trace amounts of methane, ammonia, and water vapor. The clouds in Jupiter\'s atmosphere are composed of ammonia crystals and water ice. Saturn\'s atmosphere is similar to Jupiter\'s, but it also contains a significant amount of hydrogen sulfide gas. This gas gives Saturn its distinctive yellow color. Uranus and Neptune have atmospheres that are mostly composed of hydrogen and helium, with trace amounts of methane and other gases. The blue color of Uranus and Neptune is caused by the absorption of red light by methane molecules in their atmospheres."
    }
    role: "model"
]
```

## Lessons Learnt

### File name vs Library/Package

> **Error:**<br/>
> AttributeError: partially initialized module 'langchain' has no attribute 'verbose' (most likely due to a circular import)

was due to my filename was `langchain.py` and it shadowed the actual langchain library, causing a circular import issue

### What is LangChain

LangChain is a framework that simplifies the development of applications using large language models (LLMs) by providing tools for document summarization, customizable workflows, and integration with various data sources, enabling efficient natural language processing tasks.

[More on LangChain.md](./LangChain.md)

### Generate `requirements.txt`

```bash
pip freeze > requirements.txt
```

## Credit

Thanks to this [Tutorial](https://codemaker2016.medium.com/build-your-own-chatgpt-using-google-gemini-api-1b079f6a8415) for guiding to the basics. After the tutorial I followed some Reddit posts and updated the code according to the Notices from Google.
