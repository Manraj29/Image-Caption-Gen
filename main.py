import streamlit as st
import os
import io
from PIL import Image  

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# API configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
image_model = genai.GenerativeModel("gemini-pro-vision")

def get_caption(platform, max_length, image):
    min_length = 20
    if platform is None:
        text = f"Generate a caption for this image: {image} with a max length of {max_length} and min length of {min_length}."
    else:
        text = f"Generate me a caption for this image for {platform}: {image}. which i can use on my {platform} and the caption should be of max length {max_length} and min length of {min_length}"
    response = image_model.generate_content([text, image])
    return response.text

st.title("Image Caption Generator")
st.write("This app generates a caption for an image.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# slider with min: 0, max: 100, default: 25
max_length = st.slider("Select length of the caption", 50, 100, 70)


platform = ""
if st.button("Identify image"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Generating caption...")
        caption = get_caption(platform, max_length, image)
        st.write(f"Caption: {caption}")
    else:
        st.write("Please upload an image file.")

if st.button("Insta Caption"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Generating caption for Instagram...")
        caption = get_caption("instagram", max_length, image)
        st.write(f"Caption: {caption}")
    else:
        st.write("Please upload an image file.")