import streamlit as st

# Título da Seção em Azul Vibrante
st.markdown("<h2 style='color: #00416d; font-weight: bold;'>❤️ Guia para Familiares e Amigos: Como ser uma rede de apoio real</h2>", unsafe_allow_html=True)

st.write("""
A fibromialgia é uma deficiência invisível. Por fora, a pessoa pode parecer bem, mas por dentro, 
ela está travando uma batalha exaustiva contra a dor e a fadiga. Se você convive com alguém 
que tem esse diagnóstico, veja como você pode ajudar:
""")

# --- TÓPICO 1 ---
st.markdown("### :blue[1. Acredite na dor dela]")
st.markdown("A frase 'mas você nem parece doente' é uma das que mais machucam. O maior presente que você pode dar é a validação. Quando a pessoa disser que está com dor ou exausta, acredite. Não questione a intensidade nem compare com dores comuns que você já sentiu.")

# --- TÓPICO 2 ---
st.markdown("### :blue[2. Entenda que a disposição oscila]")
st.markdown("A fibromialgia é imprevisível. A pessoa pode estar ótima de manhã e, à tarde, não conseguir levantar do sofá. Não é 'falta de vontade' ou desculpa para cancelar compromissos; é a biologia do corpo dela agindo. Seja compreensivo com cancelamentos de última hora.")

# --- TÓPICO 3 ---
st.markdown("### :blue[3. Ofereça ajuda em tarefas específicas]")
st.write("Em vez de perguntar 'precisa de alguma coisa?', ofereça ajuda prática:")
st.markdown("- **'Posso passar no mercado para você hoje?'**")
st.markdown("- **'Quer que eu leve as crianças na escola?'**")
st.markdown("- **'Posso te ajudar a lavar a louça hoje para você descansar?'**")
st.write("Pequenos esforços físicos poupados podem significar muito para quem vive com fadiga crônica.")

# --- TÓPICO 4 ---
st.markdown("### :blue[4. Incentive, mas não pressione]")
st.markdown("O exercício é essencial, mas em dias de crise, é impossível. Incentive a caminhada ou a fisioterapia nos dias bons, mas respeite o limite nos dias de crise. Não force a barra com frases como 'você precisa se esforçar mais'.")

# --- TÓPICO 5 ---
st.markdown("### :blue[5. Esteja presente no silêncio]")
st.markdown("Às vezes, a pessoa só precisa de companhia enquanto descansa, sem a pressão de ter que conversar ou ser produtiva. O acolhimento silencioso é uma forma poderosa de amor.")

# Recado para acompanhantes em destaque
st.info("""
📢
"Você não precisa entender tecnicamente como a fibromialgia funciona para ser um bom apoio. O que cura o isolamento do paciente não é o remédio, é a empatia. Ser uma rede de apoio significa caminhar ao lado, no ritmo que a pessoa consegue andar naquele dia."
""")

st.image("imagens/heart.gif")

# --- SEÇÃO 5: RELATOS ---
st.markdown("<h2 style='color: #00416d; font-weight: bold;'>💬 Espaço de Acolhimento</h2>", unsafe_allow_html=True)

with st.form("form_relato"):
    nome = st.text_input("Seu Nome (Opcional)")
    mensagem = st.text_area("Sua mensagem de apoio:")
    if st.form_submit_button("Enviar Mensagem"):
        st.success("Obrigado por compartilhar sua força!")