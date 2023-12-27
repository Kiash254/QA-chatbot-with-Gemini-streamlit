#load dotenv
from dotenv import load_dotenv
load_dotenv()
#streamlit
import streamlit as st
#os
import os
#google.generativeai as genai
import google.generativeai as genai
#import PIL
from PIL import Image

#use configure to set the api key
genai.configure(api_key=os.getenv("Google_api_key"))

model=genai.GenerativeModel('gemini-pro-vision')

def  get_gemini_response(input,image,prompt):
    resesponse=model.generate_content([input,image[0],prompt])
    return resesponse.text

#streamlit set page config
st.set_page_config(page_title="MultiLanguage Invoice Extractor",page_icon="🤖",layout="centered",initial_sidebar_state="auto")

#set the header as Gemini pro application
st.header("Gemini pro application")

#set the input field
input=st.text_input("input:",key="input")
upload_file=st.file_uploader("Upload Image",type=['png','jpeg','jpg'])

image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
    
submit=st.button("Tell me about the invoice")

input_prompt="This is an invoice for a purchase of a laptop. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020. The invoice is for a laptop that was purchased on 12/12/2020."

if submit:
    response=get_gemini_response(input,[image],input_prompt)
    st.subheader("The Response is:")
    st.write(response)