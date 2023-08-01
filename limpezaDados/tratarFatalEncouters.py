import streamlit as st
import pandas as pd
import os

def months_to_years(months_str):
    try:
        if 'months' in months_str:
            months = float(months_str.split()[0])
            years = months / 12.0
            return round(years, 2)
        else:
            return months_str
    except:
        return None
def main():
    '''st.title("Análise de Tipos e Valores Nulos do Dataset")'''

    
    file_path = "..\\data\\fatal_encounters_dot_org_updated_2.csv"
    df = pd.read_csv(file_path)

    st.subheader("Visão Geral do Conjunto de Dados")
    st.dataframe(df)

    '''st.subheader("Informações sobre os Tipos de Dados e Valores Nulos")
    st.write("Número de Linhas:", df.shape[0])
    st.write("Número de Colunas:", df.shape[1])
    
    
    st.write("Tipos de Dados das Colunas:")
    st.write(df.dtypes)

    
    st.write("Valores Nulos por Coluna:")
    st.write(df.isnull().sum())

    
    df["Subject's age"] = df["Subject's age"].apply(months_to_years)

    st.subheader("Conjunto de Dados após o Tratamento")
    st.dataframe(df)

    
    df.to_csv(file_path, index=False)

    st.success("Valores na coluna 'Subject's age' que contêm 'months' foram tratados e o arquivo CSV foi atualizado localmente!")'''
    
    
if __name__ == "__main__":
    main()