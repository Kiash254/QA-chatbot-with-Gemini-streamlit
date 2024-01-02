import os
from dotenv import load_dotenv
from gradientai import Gradient
import streamlit as st

# Load environment variables from .env file
load_dotenv()

GRADIENT_WORKSPACE_ID = os.getenv('GRADIENT_WORKSPACE_ID')
GRADIENT_ACCESS_TOKEN = os.getenv('GRADIENT_ACCESS_TOKEN')

def main():
    gradient = Gradient()

    base_model = gradient.get_base_model(base_model_slug="nous-hermes2")

    new_model_adapter = base_model.create_model_adapter(
        name="Krishmodel"
    )

    samples=[
        {"inputs":"### Instruction: Who is Samuel Kiando? \n\n### Response: Samuel kiando is a student in karatina university  and he is also a data scientist who is pationate in full stack web development and he is good in a couple f framework such as DJango,flask,streanlit,langchain and many things in the field of data scinece"},
        {"inputs":"### Instruction: Who is this person named samuel kiando? \n\n### Response: He is a male student who does programming and enjoys doing generative AI"},
        {"inputs":"### Instruction: What do you know about Samuel kiando? \n\n### Response: Samuel Loves coding, travelling, Partying,hiking and joking with friends"},
        {"inputs":"### Instruction: Can you tell me about Samuel kiando? \n\n### Response: Samuel Kiando is a student,Web developer,and loves Data Science And AI and LLM's"}
    ]

    ## Lets define parameters for finetuning
    num_epochs=3
    count=0
    while count<num_epochs:
      new_model_adapter.fine_tune(samples=samples)
      count=count+1

    st.title('Ask about Samuel Kiando')
    user_input = st.text_input("Enter your question here:")
    if st.button('Generate'):
        sample_query = f"### Instruction: {user_input} \n\n ### Response:"
        completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
        st.text_area("Response:", value=completion, height=200)

    new_model_adapter.delete()
    gradient.close()

if __name__ == "__main__":
    main()