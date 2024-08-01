#Q&A chatbot
import os

from langchain_community.llms import OpenAI, HuggingFaceHub
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

openai_api_key=os.getenv("OPENAI_API_KEY")


## Function to load OpenAI model and get response
def get_openai_response(question):
    #llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    #response = llm(question)
    llm_huggingface = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.6, "max_length": 256})
    response=llm_huggingface.predict(question)
    return response

## initialize our streamlit app
st.set_page_config(
    page_title="Q&A ChatBot"
)

st.header("Lanchain ChatBot")

input = st.text_input("Input: ", key="input")
if input:
    response=get_openai_response(input)

submit = st.button("Ask the question")

## If ask button is clicked 
if submit:
    st.subheader("The response is ")
    st.write(response)