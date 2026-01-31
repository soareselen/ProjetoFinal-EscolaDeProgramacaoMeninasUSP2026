import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("TESTE Animações do Lottie no Streamlit")

def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()


st.components.v1.html(
    """
    <iframe
        src="https://lottie.host/embed/b7562919-d97a-48ba-84c9-a386ca7797f1/G3LsyAyVCy.lottie"
        style="width: 250px; height: 300px; border: none; justify-content: center;"
    ></iframe>
    """,
    height=320, 
)
