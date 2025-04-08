from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_content(input_prompt,image):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input_prompt,image])
    return response.text


st.set_page_config("Calory Advisor")
st.title("Calory Advisor app")

uploaded_file=st.file_uploader("Upload an Image",type=["jpg","png","jpeg"])
submit=st.button("Submit")
image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,use_column_width=True,caption="uploaded image")

input_prompt="""
You are an expert nutritionist, and can analyse the constituents in the food. I want you to give an estimate of
constituents in the food items in the given format with carbohydrates, proteins, fats, fibres etc.
    1) Carbohydrates : ______
    2) Proteins: ______
    3) Fats: ______
    4) Fibres: ____
    Also as a conclusion, please justify if the food item is healthy or not
"""

if submit:
    response=get_gemini_content(input_prompt,image)
    st.subheader("The result is:")
    st.write(response)