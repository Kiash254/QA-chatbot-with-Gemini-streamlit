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

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model=genai.GenerativeModel('gemini-pro-vision', generation_config=generation_config, safety_settings=safety_settings)

def  get_gemini_response(input,image,prompt):
    prompt_parts = [input, image[0], prompt]
    response=model.generate_content(prompt_parts)
    return response.text

def input_image_details(upload_file):
    if upload_file is not None:
        #read the file into bytes
        bytes_data=upload_file.read()
        
        image_parts=[
            {
                "mime_type":upload_file.type,
                "data":bytes_data,
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not found")

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

input_prompt="The invoice is for a laptop that was purchased on 12/12/2020."

#if submit is clicked 
if submit:
    image_data=input_image_details(upload_file)
    response=get_gemini_response(input,image_data,input_prompt)
    st.subheader("The Response is:")
    st.write(response)