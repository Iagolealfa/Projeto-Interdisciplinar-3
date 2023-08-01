import streamlit as st
import pandas as pd

def main():
    st.title("Análise de Tipos e Valores Nulos do Dataset")

    # Carrega o conjunto de dados a partir do arquivo CSV
    file_path = "..\\data\\fatal_encounters_dot_org_updated.csv"
    df = pd.read_csv(file_path)

    st.subheader("Visão Geral do Conjunto de Dados")
    st.dataframe(df)

    st.subheader("Informações sobre os Tipos de Dados e Valores Nulos")
    st.write("Número de Linhas:", df.shape[0])
    st.write("Número de Colunas:", df.shape[1])
    
    # Obtém informações sobre os tipos de cada coluna
    st.write("Tipos de Dados das Colunas:")
    st.write(df.dtypes)

    # Verifica se há valores nulos em cada coluna
    st.write("Valores Nulos por Coluna:")
    st.write(df.isnull().sum())

if __name__ == "__main__":
    main()