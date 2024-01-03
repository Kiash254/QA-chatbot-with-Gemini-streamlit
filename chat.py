import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain.vectorstores import FAISS
# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Load the environment variables from a .env file
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Google GEMINI model and related components
chat = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5, convert_system_message_to_human=True)
embeddings_model = "models/embedding-001"  # Replace this with your specific embeddings model
vector_store = None  # Placeholder for the vector store

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

# Function to load the vector store database
def load_vector_store():
    global vector_store
    embeddings = GoogleGenerativeAIEmbeddings(model=embeddings_model)
    vector_store = FAISS.load_local("faiss_index", embeddings)

# Function to get response using Google GEMINI model
def get_gemini_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    # Ensure the conversation flow ends with a user role or function response
    st.session_state['flowmessages'].append(SystemMessage(content="user"))
    
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

# Streamlit UI components
input_text = st.text_input("Input: ", key="input")
response = get_gemini_response(input_text)
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
