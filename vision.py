import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image


load_dotenv()


genai.configure(api_key=os.environ["API_KEY"])


model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image):

    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config("Gemini Application")
input = st.text_input("Input Prompt:",key="input")

uploded_file = st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])

image =""

if uploded_file is not None:
    image = Image.open(uploded_file)
    st.image(image,caption="Uploded Image",use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)