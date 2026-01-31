import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.markdown("<h2 style='color: #00416d; font-weight: bold;'>Possíveis Tratamentos</h2>", unsafe_allow_html=True)
st.components.v1.html(
    """
    <iframe
        src="https://lottie.host/embed/2c582ddd-5531-4136-ae1c-bb139f88b6a6/waIJTdjh8b.lottie"
        style="width: 550px; height: 200px; border: none; justify-content: center;"
    ></iframe>
    """,
    height=220, 
)

st.write("Como a fibromialgia é um distúrbio de sensibilização central, o objetivo dessas estratégias não é apenas 'esticar o músculo', mas sim reeducar o cérebro a baixar o volume da dor e aumentar a produção de neurotransmissores do bem-estar, como a serotonina e a endorfina.")


st.write("Aqui estão as abordagens com as melhores evidências científicas hoje:")
st.markdown(":blue[**1. Exercícios Aeróbicos de Baixo Impacto**]")
st.markdown("Este é o *padrão ouro* do tratamento não medicamentoso. O foco não é performance, mas consistência.")
st.markdown("""
            - **Caminhada leve**: Ajuda a manter a mobilidade sem sobrecarregar o sistema nervoso.
            - **Ciclismo**: Uma excelente alternativa para quem sente muito impacto nos joelhos.
            - **Natação ou Hidroginástica**: A água aquecida (idealmente entre 30°C e 34°C) relaxa os músculos e a flutuabilidade reduz a carga nas articulações, facilitando o movimento que seria doloroso em terra firme.
            """)

st.markdown("""---""")

st.markdown(":blue[**2. Práticas de Mente e Corpo**]")
st.markdown("Essas atividades trabalham o foco e a respiração, ajudando a acalmar o sistema nervoso hiperativo.")
st.markdown("""
            - **Tai Chi e Yoga**: Estudos mostram que essas práticas são tão eficazes quanto exercícios aeróbicos para fibromialgia, pois combinam força, equilíbrio e meditação.
            - **Mindfulness (Atenção Plena)**: Ajuda a mudar a relação do paciente com a dor, reduzindo a resposta de "luta ou fuga" do corpo e diminuindo o estresse, que é um gatilho clássico de crises.
""")

st.markdown("""---""")

st.markdown(":blue[**3. Higiene do Sono (Crucial)**]")
st.markdown("Como a dor piora se você não dorme, e você não dorme porque sente dor, quebrar esse ciclo é vital:")
st.markdown("""
            - **Rotina rígida**: Deitar e acordar sempre no mesmo horário.
            - **Bloqueio de luz azul:** Evitar telas (celular/TV) pelo menos 1 hora antes de dormir.
            - **Ambiente:** O quarto deve ser escuro, silencioso e levemente fresco.
            """)

st.markdown("""---""")

st.markdown(":blue[**4. Terapia Cognitivo-Comportamental (TCC)**]")
st.markdown("Não se trata de dizer que a dor está 'na sua cabeça', mas sim de fornecer ferramentas práticas para:")
st.markdown("""
            - Identificar **gatilhos emocionais** que pioram a dor física.
            - Combater a **catastrofização** (o pensamento de que a dor nunca vai passar), que fisiologicamente aumenta a percepção dolorosa.
            """)

st.markdown("""---""")

st.markdown(":blue[**5. Ajustes Alimentares**]")
st.markdown("Embora não exista uma 'dieta da fibromialgia', algumas mudanças ajudam a reduzir o estado de irritabilidade do corpo:")
st.markdown("""
            - **Redução de Ultraprocessados:** Alimentos muito industrializados podem aumentar a percepção de fadiga.
            - **Magnésio e Ômega-3:** Consultar um nutricionista para avaliar a suplementação, já que o magnésio atua no relaxamento muscular e o ômega-3 tem propriedades protetoras.
            """)

st.markdown("""---""")

st.image("imagens/tabela comparativa.png")

st.markdown("""---""")

st.info("💡 O segredo para quem tem fibromialgia é a regra do *Start Low, Go Slow* (Comece baixo, vá devagar). Tentar fazer muito exercício de uma vez pode causar um efeito rebote de dor.")

