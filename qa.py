from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("Google_api_key"))

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def get_gemini_response(question):  
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Question Answer chat bot",page_icon=":gem:",layout="wide")

st.sidebar.title("Welocome Gemini Pro Chatbot")
st.header("Interactive Chatbot with Gemini Pro")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

input_question=st.text_input("Input",key="input_question")
submit=st.button("Ask Question")

if input_question and submit:
   response=get_gemini_response(input_question)
   st.session_state['chat_history'].append(("You", input_question))
   st.subheader("The Response is:")
   for chunk in response:
       st.write(chunk.text)
       st.session_state['chat_history'].append(("BOT", chunk.text))

st.subheader("Chat History")
for role,  text in  st.session_state['chat_history']:
    st.write(f"{role}: {text}")