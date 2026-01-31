import streamlit as st

#PROJETO FINAL ESCOLA DE PROGAMAÇÃO WEB PARA MENINAS
# PRECISA:
#● Menus de navegação
#● Textos e imagens
#● Formulários
#● Animações
#● Aplicação de estilos e temas
#um banco de dados, permitindo o cadastro, a
#consulta e a edição de informações.


st.title(":blue[FIBROMIALGIA]")

# Divisor abaixo do título
st.markdown("<hr style='border: 2px solid #2F4F4F; margin-top: 0px; margin-bottom: 10px;'>", unsafe_allow_html=True)

# Subtítulo colorido
st.markdown("<h3 style='color: #4682B4;'>Entenda o que é a síndrome, que foi reconhecida como deficiência em 2026.</h3>", unsafe_allow_html=True)
st.image("imagens/equeleto-gif.gif")

st.warning("**As informações aqui contidas são de caráter informativo. Para orientações jurídicas específicas ou solicitações de benefícios, consulte um advogado especializado ou a Defensoria Pública da sua região.**")

# CÓDIGO HTML
# html_code = """
# <h1 style = 'color: pink>Esse é um texto rosa</h>
# <p style = 'color:purple>Esse é um texto roxo</p>

