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
        {"inputs":"### Instruction: Who is Eugene Muasya? \n\n### Response: Eugene Muasya is a student at Karatina University, an amateur full stack developer, and a data analyst using blockchains. He also enjoys playing darts as an indoor activity. You can check out his work on [GitHub](https://github.com/YourGitHubProfile)."},
        {"inputs":"### Instruction: Who is this person named Eugene Muasya? \n\n### Response: Eugene Muasya is a male student who enjoys programming and data analysis using blockchains. He shares his thoughts and projects on [Twitter](https://twitter.com/home)."},
        {"inputs":"### Instruction: What do you know about Eugene Muasya? \n\n### Response: Eugene loves coding, data analysis, and playing darts. He maintains a professional profile on [LinkedIn](https://www.linkedin.com/feed/)."},
        {"inputs":"### Instruction: Can you tell me about Eugene Muasya? \n\n### Response: Eugene Muasya is a student, amateur full stack developer, and loves data analysis using blockchains. You can learn more about him and his projects on his [GitHub](https://github.com/724502) profile."}
    ]
    ## Lets define parameters for finetuning
    num_epochs=3
    count=0
    while count<num_epochs:
      new_model_adapter.fine_tune(samples=samples)
      count=count+1

    st.title('Ask me  about the Question have for Fine Tuned data ')
    user_input = st.text_input("Enter your question here:")
    if st.button('Generate'):
        sample_query = f"### Instruction: {user_input} \n\n ### Response:"
        completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
        st.text_area("Response:", value=completion, height=200)

    new_model_adapter.delete()
    gradient.close()

if __name__ == "__main__":
    main()