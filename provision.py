import streamlit as st
from pathlib import Path
import google.generativeai as genai

def main():
    st.title('Image Description Generator')

    st.sidebar.header('Gemini Pro Vision AI')
    st.sidebar.write('Hello, please upload an image and the model will generate a description of the image.')

    genai.configure(api_key="AIzaSyDMJUY5I2f849g51nRE20jde8jE-yOBZ2w")

    # Set up the model
    generation_config = {
        "temperature": 0.8,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    uploaded_file = st.file_uploader("Choose an image...", type="png")
    user_question = st.text_input("Ask a question about the image:")

    if uploaded_file is not None and user_question:
        if st.button('Submit'):
            image_parts = [{"mime_type": "image/png", "data": uploaded_file.getvalue()}]
            prompt_parts = [user_question + "\n", image_parts[0]]
            response = model.generate_content(prompt_parts)
            st.write(response.text)

if __name__ == "__main__":
    main()