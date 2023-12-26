#streamlit
import streamlit as st
#os
import os
#google.generativeai as genai
import google.generativeai as genai

#PIL
from PIL import Image
#use configure to set the api key
genai.configure(api_key=os.getenv("Google_api_key"))

model=genai.GenerativeModel('gemini-pro-vision')
#function to load gemini model and response
def load_gemini_model(input,image):
    if input != "":
        response=model.generate_content([input,image])
        
    else:
        response=model.generate_content(image)
    return response.text

#set up the streamlit application

#set the page_config as Upload an image  Bot with Gemini model and provide a description
st.set_page_config(page_title="Upload an image  Bot with Gemini model",page_icon="🤖",layout="centered",initial_sidebar_state="auto")

#set the header as Gemini pro application
st.header("Gemini pro application")

#set the input field
input=st.text_input("Input Promot:",key="input")

#provide a file uploader
upload_file=st.file_uploader("Choose an image....",type=['png','jpeg','jpg'])

image=""

if upload_file is not None:
    image=upload_file.read()
    st.image(upload_file,caption="Uploaded Image",use_column_width=True)
    
    
#create a submit button to tell about the image
submit=st.button("Tell about the image")

#if submit button is clicked
if submit:
    response=load_gemini_model(input,image)
    st.subheader("The Response is:")
    st.write(response)