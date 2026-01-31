import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.markdown("<h2 style='color: #00416d; font-weight: bold;'>Leis e Direitos</h2>", unsafe_allow_html=True)

st.components.v1.html(
    """
    <iframe
        src="https://lottie.host/embed/a8c28aaf-5908-472d-9bf2-34aa19dffc3c/48Q8r3nLRQ.lottie"
        style="width: 300px; height: 300px; border: none; justify-content: center;"
    ></iframe>
    """,
    height=250, 
)

st.markdown(":blue[**O Marco Histórico: Lei Federal nº 15.176/2025**]")
st.markdown("Sancionada em julho de 2025, ela alterou o cenário nacional ao estabelecer que:")
st.markdown("- **Reconhecimento como PcD**: A partir de janeiro de 2026, a pessoa com fibromialgia é oficialmente considerada Pessoa com Deficiência (PcD) para todos os efeitos legais em todo o território nacional.")
st.markdown("- **Equiparação ao Estatuto da Pessoa com Deficiência:** Isso significa que os diagnosticados passam a ter os mesmos direitos garantidos pela Lei nº 13.146/2015 (Lei Brasileira de Inclusão).")
st.markdown("- **Avaliação Biopsicossocial:** Para acessar os benefícios, o paciente deve passar por uma avaliação feita por equipe multiprofissional, que analisará os impedimentos físicos, fatores psicológicos e limitações sociais.")

st.markdown("""---""")

st.markdown(":blue[**Lei nº 14.705/2023: Atendimento no SUS**]")
st.markdown("Antes do reconhecimento como deficiência, esta lei de 2023 já garantia o suporte clínico. Ela define que o SUS deve oferecer:")
st.markdown("- **Atendimento Multidisciplinar:** Equipes com médicos, psicólogos, nutricionistas e fisioterapeutas.")
st.markdown("- **Acesso a Tratamentos:** Garantia de medicamentos e modalidades terapêuticas (como atividade física supervisionada) específicas para a dor crônica.")

st.markdown("""---""")

st.markdown(":blue[**O Cartão de Identificação**]")
st.markdown("Muitos estados e municípios (como São Paulo, Paraíba e DF) já emitiam a Carteira de Identificação da Pessoa com Fibromialgia (CIPFIBRO). Com a lei nacional, esse documento ganha ainda mais força para evitar constrangimentos em locais públicos, comprovando a *deficiência invisível* sem a necessidade de carregar laudos extensos o tempo todo.")

st.warning("É importante ressaltar que, embora a lei seja federal, a emissão do cartão de identificação costuma ser de responsabilidade das Secretarias de Saúde ou de Assistência Social de cada município ou estado.")

st.markdown("""---""")

