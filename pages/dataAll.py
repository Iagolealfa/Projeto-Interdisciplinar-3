import streamlit as st
import pandas as pd
def carregar_dataset():
    
    with st.expander('fatal_encounters_dot_org'):
        fatal_encounters_dot_org = pd.read_csv('dataframeSujo/fatal_encounters_dot_org.csv')
        st.write(fatal_encounters_dot_org)
    with st.expander('PoliceKillings'):
        dataPoliceKillings = pd.read_csv("dataframeSujo/police_killings_MPV.csv")
        st.write(dataPoliceKillings)
    with st.expander('ShareRaceByCity'):
        dataShareRaceByCity= pd.read_csv("dataframeSujo/ShareRaceByCity.csv")
        st.write(dataShareRaceByCity)

def cabecalho():
    st.title("Data Bucket")
    st.subheader("Datasets completos")
def run():
    cabecalho()
    carregar_dataset()

run()