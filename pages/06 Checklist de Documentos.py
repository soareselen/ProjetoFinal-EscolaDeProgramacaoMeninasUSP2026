import streamlit as st
 

st.markdown("<h2 style='color: #00416d; font-weight: bold;'>Checklist de Documentos</h2>", unsafe_allow_html=True)
st.write("Para garantir seus direitos, mantenha uma pasta com os documentos atualizados.")

# --- SEÇÃO 1 ---
st.markdown("### :blue[1. Documentação Médica (A prova principal)]")

st.components.v1.html(
    """
    <iframe
        src="https://lottie.host/embed/b371924e-ba67-441c-b683-1d32ee9c527c/Qd5ftOc29P.lottie"
        style="width: 200px; height: 300px; border: none; justify-content: center;"
    ></iframe>
    """,
    height=300, 
)


st.markdown("- **Laudo Médico Detalhado:** Deve conter o diagnóstico claro, o código da doença (O atualizado CID-11 MG30.01) e a descrição das limitações que a dor causa no seu dia a dia.")
st.info("💡 **Lembre-se** O laudo deve ter data recente (geralmente menos de 6 meses).")
st.warning("📝 **Dica:** Em novas consultas, peça para o médico já incluir o código MG30.01 em seus laudos.")
st.markdown("- **Receitas e Prescrições:** Cópias de todas as receitas de medicamentos que você utiliza.")
st.markdown("- **Exames Complementares:** Guarde exames que descartem outras doenças, pois eles reforçam o diagnóstico clínico.")
st.markdown("- **Relatórios de Terapias:** Peça aos profissionais um breve relatório sobre a sua evolução e limitações.")

# --- SEÇÃO 2 ---
st.markdown("### :blue[2. Documentos Pessoais]")

st.markdown("- **RG e CPF** (ou CNH válida).")
st.markdown("- **Comprovante de Residência** atualizado (últimos 3 meses).")
st.markdown("- **Cartão Nacional de Saúde** (Cartão do SUS).")
st.markdown("- **Foto 3x4 recente** (necessária para a emissão da Carteira de Identificação).")

# --- SEÇÃO 3 ---
st.markdown("### :blue[3. Para Fins Previdenciários ou Isenções]")

st.markdown("- **Carteira de Trabalho (CTPS):** Digital ou física.")
st.markdown("- **CNIS:** Pode ser retirado no portal Meu INSS.")
st.markdown("- **Laudo de Avaliação Biopsicossocial:** Conforme a nova Lei Federal de 2025.")

# --- SEÇÃO 4 ---
st.markdown("### :blue[4. Para o Cartão de Estacionamento]")

st.markdown("- **Formulário específico** da prefeitura ou órgão de trânsito local (DSV/Detran).")
st.markdown("- **Cópia do laudo médico** confirmando a deficiência/limitação de mobilidade.")

st.info("💡 **Lembre-se:** O perito ou o funcionário público que analisará seu pedido não te conhece. O laudo médico é a sua voz e a sua prova. Se estiver incompleto, o seu direito pode ser negado!")

# O conteúdo que será baixado (formatado para leitura fácil)
checklist_texto = """
CHECKLIST DE DOCUMENTOS PARA FIBROMIALGIA (LEI FEDERAL 2026)
----------------------------------------------------------

1. DOCUMENTAÇÃO MÉDICA
- Laudo Médico Detalhado (CID-10 M79.7 ou CID-11 MG30.01)
- Descrição de limitações (locomoção, fadiga, dor crônica)
- Receitas e Prescrições atualizadas
- Exames Complementares (para descarte de outras patologias)
- Relatórios de Fisioterapia/Terapias

2. DOCUMENTOS PESSOAIS
- RG e CPF / CNH
- Comprovante de Residência (últimos 3 meses)
- Cartão do SUS
- Foto 3x4

3. FINS PREVIDENCIÁRIOS / ISENÇÕES
- Carteira de Trabalho (CTPS)
- Extrato CNIS (Meu INSS)
- Laudo de Avaliação Biopsicossocial

4. CARTÃO DE ESTACIONAMENTO
- Formulário do Detran/Prefeitura
- Cópia do Laudo Médico indicando limitação de mobilidade
----------------------------------------------------------
Gerado pelo App Fibromialgia - 2026
"""

# Botão de Download
st.download_button(
    label="📥 Baixar Checklist para Imprimir (TXT)",
    data=checklist_texto,
    file_name="checklist_fibromialgia.txt",
    mime="text/plain",
)

st.caption("Dica: Ao abrir o arquivo, você pode imprimir ou salvar como PDF no seu computador/celular.")
