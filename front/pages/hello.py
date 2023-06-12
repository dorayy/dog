import requests
import streamlit as st
from PIL import Image

st.title("Calculatrice Simple")

# Utilisez le File Uploader de Streamlit pour obtenir l'image téléversée
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Si une image est téléversée, affichez-la à l'utilisateur
if uploaded_file is not None:
    image = uploaded_file.read()
    st.image(image, caption='Uploaded Image.')

if st.button('Envoyer'):
    # Envoyer l'image à l'API

    if uploaded_file.name.endswith(".png"):
        image = Image.open(uploaded_file)
        image = image.convert('RGB')
        image.save('image.jpg')
        image = open('image.jpg', 'rb')


    files = {'file': ('image.jpg', image)}
    headers = {"Content-Disposition": "attachment"}
    endPoint = "http://127.0.0.1:8000/api/upload"

    # send image file to api without request
    response = requests.post(endPoint, files=files, headers=headers)

    # log the response
    st.write(response.json())
