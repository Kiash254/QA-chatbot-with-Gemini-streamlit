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