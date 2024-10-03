import streamlit as st   
from langchain_groq import ChatGroq

def get_response(question):
    llm = ChatGroq(
    model_name="llama-3.2-90b-text-preview",  
    temperature=0,
    groq_api_key="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")
    response=llm.invoke(question)
    return response.content

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")
input=st.text_input("Query Console",key="input")
response = get_response(input)



submit=st.button("Enter")

if submit:
    st.subheader("The response is")
    st.write(response)