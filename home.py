import streamlit as st

st.set_page_config(
    page_title = "Porcos Fascistas",
    menu_items = {
        'About': "TESTE DO ABOUT"
    }
)

st.title("Análise de padrões de letalidade policial nos Estados Unidos")
st.text('''Este projeto tem como objetivo analisar uma base de dados com informações de 
encontro fatais com a policia nos estados unidos, utilizando mineração de dados
e aprendizado de máquina''')
st.text('''Projeto desenvolvido para disciplina Projeto Interdisciplinar 3 do curso de Sistema
de Informação da Universidade Federal Rural de Pernambuco''')
st.text('''Grupo:
- Antonio Neto
- Caio Mizan
- Iago Leal
''')
st.text("Recife, 2023")