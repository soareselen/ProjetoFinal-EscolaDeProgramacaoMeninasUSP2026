import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("Animações do Lottie no Streamlit")

def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()


url_animacao = "https://lottie.host/807e1553-6202-45e0-9118-095208479e00/87O00jF8H6.json"
               

animacaoEmail = carregar_animacao(url_animacao)

st_lottie(animacaoEmail, key="animacaoEmail")