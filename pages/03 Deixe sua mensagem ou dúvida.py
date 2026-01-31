import streamlit as st

st.subheader("Quer compartilhar sua experiência ou tirar alguma dúvida? Nos mande uma mensagem:")
st.write("Para nos mandar sua mensagem, preencha o formulário, conforme solicitado abaixo:")

with st.form("formCadastro"):
   nome = st.text_input("Informe o seu nome completo", placeholder="Nome Completo")
   idade = st.number_input("Informe a sua idade", min_value=10, max_value=100, step=1)
   dataNascimento = st.date_input("Dt. Nascimento", format="DD/MM/YYYY")
   portador = st.selectbox(
    "Você é portador(a) da Fibromialgia?:",
    ('Não', 'Sim') # A primeira opção é a pré-selecionada
)
   texto = st.text_input("Escreva a sua mensagem", placeholder="Dúvidas, experiências, dicas, palavras de motivação e etc.")
   botaoFormCadastro = st.form_submit_button("Enviar")
   if botaoFormCadastro:
      st.write("Mensagem enviada! :)")
   if not nome:
        st.error("Preencha o NOME")
   #elif len(nome) <=6:
        #st.error("Nome precisa ter mais que 6 letras")
   #else:
  #      st.write("Nome:", nome)
  #      st.write("Idade:", idade)
  #     st.write("Data de Nascimento:", dataNascimento)
  #      st.write("Portador de Fibromialgia?", portador)
  #      st.write("Mensagem:", texto)