import streamlit as st
import pandas as pd
def carregar_dataset():
    
    with st.expander('Dados Sujos'):
        fatal_encounters_dot_org = pd.read_csv('dataframeSujo/fatal_encounters_dot_org.csv')
        st.write(fatal_encounters_dot_org)
    with st.expander('Dados tratados'):
        fatal_encounters_dot_org = pd.read_csv('data/fatal_encounters_tratado.csv')
        st.write(fatal_encounters_dot_org)
def cabecalho():
    st.title("Data Bucket")
    st.subheader("Datasets completos")
def run():
    cabecalho()
    carregar_dataset()

run()