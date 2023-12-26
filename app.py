#load the env variables using the dotenv package
from dotenv import load_dotenv
load_dotenv()
#streamlit
import streamlit as st
#os
import os
#google.generativeai as genai
import google.generativeai as genai

#use configure to set the api key
genai.configure(api_key=os.getenv("Google_api_key"))

model=genai.GenerativeModel('gemini-pro')
#function to load gemini model and response
def load_gemini_model(question):
    response=model.generate_response(question)  # Corrected here
    return response.text  # Corrected here

#setting up the Streamlit application

#set the page_config as Question Answering Bot with Gemini model
st.set_page_config(page_title="Question Answering Bot with Gemini model",page_icon="🤖",layout="centered",initial_sidebar_state="auto")

#set the header s Gemini pro application
st.header("Gemini pro application")

#set the input field 
input=st.text_input("input:",key="input")
submit=st.button("ASK a QUESTION")

#when a submit button is clicked
if submit:
    response=load_gemini_model(input) 
    st.subheader("The Response is:")  
    st.write(response)