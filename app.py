import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

#Gemini model
model = genai.GenerativeModel('gemini-pro')

def main():
    
    st.title("Gemini-Api App")

    
    question = st.text_input("Enter your prompt:")

    if st.button("Run"):
        response = model.generate_content(question)
        st.text_area("Cevap:", response.text, height=300)

if __name__ == "__main__":
    main()