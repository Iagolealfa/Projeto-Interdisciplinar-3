import streamlit as st
import pandas as pd
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

def cabecalho():
    st.title("Data Bucket")
    st.subheader("Datasets completos")
def run():
    cabecalho()
    carregar_dataset()

run()