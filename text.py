import streamlit as st
from transformers import pipeline

def main():
    st.title('Text Generation with Hugging Face Transformers')

    st.sidebar.header('Instructions')
    st.sidebar.write('Please input a text and the model will generate a continuation of the text.')

    # Set up the model
    pipe = pipeline("text2text-generation", model="google/flan-t5-large")

    user_input = st.text_input("Input text:")
    if user_input:
        if st.button('Submit'):
            response = pipe(user_input)[0]['generated_text']
            st.write(response)

if __name__ == "__main__":
    main()