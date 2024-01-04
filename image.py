import streamlit as st
from PIL import Image
from io import BytesIO
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import tempfile

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def main():
    st.title('Image Analysis with Langchain Model')

    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, use_column_width=True)

    question = st.text_input('Enter a question about the image')
    if st.button('Submit') and image_file is not None:
        # Save the image file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f:
            image.save(f, "JPEG")
            temp_image_url = f.name

        llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
        message = HumanMessage(
            content=[
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": temp_image_url},
            ]
        )
        result = llm.invoke([message])
        st.write('Result: ', result)

if __name__ == '__main__':
    main()