import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Police Shooting",
    layout = "wide")

def carregar_dataset():
    
    with st.expander('fatal_encounters_dot_org'):
        fatal_encounters_dot_org = pd.read_csv('data\\fatal_encounters_dot_org.csv')
        st.write(fatal_encounters_dot_org)
    with st.expander('PoliceKillings'):
        dataPoliceKillings = pd.read_csv("data\police_killings_MPV.csv")
        st.write(dataPoliceKillings)
    with st.expander('ShareRaceByCity'):
        dataShareRaceByCity= pd.read_csv("data\ShareRaceByCity.csv")
        st.write(dataShareRaceByCity)
    with st.expander('ShootingsWash'):
        shootingsWash = pd.read_csv("data\shootings_wash_post.csv")
        st.write(shootingsWash)

def barra_Lateral():
    opcoes = ["Informação 1", "Informação 2"]
    selecao = st.sidebar.selectbox("Selecione uma opção", opcoes)

def main():
    st.title("Análise exploratória de dados")
    st.subheader("Datasets completos")
    barra_Lateral()
    carregar_dataset()

if __name__ == "__main__":
    main()