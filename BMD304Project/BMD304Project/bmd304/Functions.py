import requests
import streamlit as st
import numpy as np
import database as db
from PIL import Image, ImageOps
import base64
import io
import json
import sqlDatabase as sqDb

from datetime import date

# Define API endpoint
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Set your OpenAI API key
API_KEY = "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"


def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = (
        """
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    """
        % bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)


def import_predict(image_data, model):
    size = (512, 512)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def get_all_patient():
    items = sqDb.fetch_all_patients()
    patient = [item[0] for item in items]
    return patient


def image_to_json(uploaded_image):
    # Check if an image was uploaded
    if uploaded_image is not None:
        # Read the contents of the image
        image_content = uploaded_image.read()

        # Create a byte stream from the image content
        image_stream = io.BytesIO(image_content)

        # Convert the image data to a base64 string
        encoded_image = base64.b64encode(image_content).decode("utf-8")

        # Store the base64 string in a JSON object
        json_data = {"image_name": uploaded_image.name, "image_content": encoded_image}

        # Serialize the JSON object to a string
        json_string = json.dumps(json_data)

        return json_string
    else:
        return None


def json_to_image(json_string):
    # Deserialize the JSON string to a dictionary
    json_data = json.loads(json_string)

    # Get the base64 encoded image data from the dictionary
    encoded_image = json_data["image_content"]

    # Decode the base64 encoded image data to bytes
    image_bytes = base64.b64decode(encoded_image)

    # Create a byte stream from the image data
    image_stream = io.BytesIO(image_bytes)

    # Display the image using Streamlit
    st.image(image_stream)


def send_message(message):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_OPENAI_API_KEY",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    # Extract the model's reply from the API response
    reply = response_data["choices"][0]["message"]["content"]
    return reply


def calculate_age(dob):
    if dob.year is None:
        print("No data provided")
        return None
    today = date.today()
    age = today.year - dob.year

    # Check if birthday has already occurred this year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1

    return age
