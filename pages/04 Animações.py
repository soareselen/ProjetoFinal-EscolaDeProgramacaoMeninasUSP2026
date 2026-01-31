import requests
import streamlit as st

st.title("Animações do Lottie no Streamlit")

def carrefar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()


#url_animacao = COLOCAR A URL DA ANIMAÇÃO, o site da lottie,
               #não quer logar

#animacaoChat (variável da animação) = carregar_animacao(url_animacao)
#st_lottie(animacaoChat, key="animacaoChat")