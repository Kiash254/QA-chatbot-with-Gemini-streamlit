import os
import streamlit as st
from transformers import pipeline
from dotenv import load_dotenv

def main():
    st.title('Text Generation with Hugging Face Transformers')

    st.sidebar.header('Instructions')
    st.sidebar.write('Please input a text and the model will generate a continuation of the text.')

    load_dotenv()  # take environment variables from .env.
    hugging_face_api_key = os.getenv("HUGGING_FACE_API")

    # Set up the model
    pipe = pipeline("text2text-generation", model="google/flan-t5-large", api_key=hugging_face_api_key)

    user_input = st.text_input("Input text:")
    if user_input:
        if st.button('Submit'):
            response = pipe(user_input)[0]['generated_text']
            st.write(response)

if __name__ == "__main__":
    main()