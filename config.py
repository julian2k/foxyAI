import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Initialize the OpenAI client

# Check if the API key is loaded
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Please check your .env file or environment variables.")

# Streamlit Configurations
STREAMLIT_HOST = os.getenv("STREAMLIT_HOST", "localhost")
STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT", "8501"))

# OpenAI Assistant Configurations
MODEL_NAME = "gpt-4-1106-preview"
INSTRUCTIONS = "You are an academic assistant that helps teachers design lesson plans."

# Lesson Material Generator Configurations
LESSON_MATERIALS_PATH = os.getenv("LESSON_MATERIALS_PATH", "./lesson_materials/")
