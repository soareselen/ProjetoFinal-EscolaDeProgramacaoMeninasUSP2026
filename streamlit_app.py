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

st.title("Fibromialgia",)
st.header("Entenda o que é a sídrome, que foi reconhecida como deficiência em 2026.", divider=True)
st.image("imagens/equeleto-gif.gif")
st.subheader("O que é Fibromialgia?")
st.write(
    "Fibromialgia é uma síndrome crônica caracterizada por dor musculoesquelética generalizada, fadiga intensa, sono não reparador e alterações cognitivas (névoa mental). Sem cura definitiva, a condição afeta principalmente mulheres de 30 a 55 anos e é tratada com uma abordagem multidisciplinar, incluindo exercícios físicos, medicações e suporte psicológico para melhorar a qualidade de vida. ."
)

st.markdown("""---""")

st.subheader("Sintomas e Características"
             )
st.write("- Dor Difusa: Dor constante por todo o corpo, sem sinais de inflamação local, com maior sensibilidade ao toque e pressão."
         )
st.write("- Distúrbios do Sono: Sono de má qualidade, fazendo com que o paciente acorde cansado."
         )
st.write("- Sintomas Cognitivos e Emocionais: Alterações de memória, falta de concentração, ansiedade e depressão."
         )
st.write("- Outros: Formigamentos, dores de cabeça, tonturas e síndrome do intestino irritável. ")

st.markdown("""---""")

# CÓDIGO HTML
# html_code = """
# <h1 style = 'color: pink>Esse é um texto rosa</h>
# <p style = 'color:purple>Esse é um texto roxo</p>

st.subheader("Quer compartilha sua experiência ou tirar alguma dúvida? Nos mande uma mensagem:")
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