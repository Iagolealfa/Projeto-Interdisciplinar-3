import streamlit as st
import pandas as pd
import os

def main():
    st.title("Análise de Tipos e Valores Nulos do Dataset")

    
    file_path = "..\\data\\us_census_demographic_data.csv"

   
    df = pd.read_csv(file_path)

    st.subheader("Visão Geral do Conjunto de Dados")
    st.dataframe(df)

    st.subheader("Informações sobre os Tipos de Dados e Valores Nulos")
    st.write("Número de Linhas:", df.shape[0])
    st.write("Número de Colunas:", df.shape[1])
    
    
    st.write("Tipos de Dados das Colunas:")
    st.write(df.dtypes)

   
    st.write("Valores Nulos por Coluna:")
    st.write(df.isnull().sum())

    
    rows_with_null_child_poverty = df[df['ChildPoverty'].isnull()]

    st.subheader("Linhas com Valores Nulos na Coluna 'ChildPoverty'")
    st.dataframe(rows_with_null_child_poverty)

    
    child_poverty_mean = df['ChildPoverty'].mean()

    
    df['ChildPoverty'].fillna(child_poverty_mean, inplace=True)

    
    updated_file_path = os.path.join("..\\data", "us_census_demographic_data_updated.csv")
    df.to_csv(updated_file_path, index=False)

    st.subheader("Conjunto de Dados com Valores Nulos Preenchidos pela Média")
    st.dataframe(df)

    st.success("Valores nulos na coluna 'ChildPoverty' foram preenchidos pela média e o novo arquivo CSV foi salvo!")

if __name__ == "__main__":
    main()