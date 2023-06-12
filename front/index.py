import requests
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("Calculatrice Simple")

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)


# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=450,
    width=800,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# download image after click on send to streamlit button
if st.button('Save image and send to Ai'):
    # save image to local
    pil_image = Image.fromarray(canvas_result.image_data)
    if pil_image.mode == 'RGBA':
        pil_image = pil_image.convert('RGB')
    pil_image.save('draw.jpg', 'JPEG')

    # send image to api
    files = {'file': ('draw.jpg', open('draw.jpg', 'rb'))}
    headers = {"Content-Disposition": "attachment"}
    endPoint = "http://127.0.0.1:8000/api/upload"
    
    # send image file to api without request
    response = requests.post(endPoint, files=files, headers=headers)

    # log the response
    st.write(response.json())