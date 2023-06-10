import streamlit as st
import pandas as pd


def carregar_dataset():
    dataPoliceKillings = pd.read_csv("data\police_killings_MPV.csv")
    return dataPoliceKillings

def main():
    st.title("Análise exploratória de dados")
    with st.expander('Dataset completo'):
        dataset = carregar_dataset()
        st.write(dataset)

if __name__ == "__main__":
    main()