import base64
import streamlit as st

def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    return base64_image

def set_background(image_path):
    base64_image = get_base64_of_image(image_path)
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{base64_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .block-container {{
            padding: 2rem;
            background: rgba(0, 0, 0, 0.75);
            border-radius: 10px;
        }}
        h1, h2, h3, h4, h5, h6, p {{
            color: white !important;
        }}
        .stSelectbox > div > div {{
            max-width: 400px;  /* Réduire la largeur de la barre de recherche */
            margin: 0 auto;  /* Centrer la barre de recherche */
        }}
        </style>
        """, unsafe_allow_html=True)
