import streamlit as st
from base64 import b64encode
import os

# Afficher ou cacher le contenu de la page HTML
if st.checkbox("Afficher le notebook"):
    html_file = open(os.path.join(os.getcwd(), "inception-dog.html"), 'r', encoding='utf-8')
    page_content = html_file.read()
    st.components.v1.iframe(src="data:text/html;base64," + b64encode(page_content.encode()).decode(), width=700, height=600, scrolling=True)