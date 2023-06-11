import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Police Shooting",
    layout = "wide",
    
)

def carregar_dataset():
    dataPoliceKillings = pd.read_csv("data\police_killings_MPV.csv")
    return dataPoliceKillings

def main():
    st.title("Análise exploratória de dados")
    barra_Lateral()
    with st.expander('Dataset completo'):
        dataset = carregar_dataset()
        st.write(dataset)


def barra_Lateral():
    opcoes = ["Informação 1", "Informação 2"]
    selecao = st.sidebar.selectbox("Selecione uma opção", opcoes)

if __name__ == "__main__":
    main()