import streamlit as st
import pandas as pd
import os
def remove_variation(age_str):
    try:
        return age_str.replace('3 day', '0.0082')
    except:
        return age_str
def remove_s(age_str):
    try:
        return age_str.replace('s', '')
    except:
        return age_str
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

    '''st.subheader("Visão Geral do Conjunto de Dados")
    st.dataframe(df)

    st.subheader("Informações sobre os Tipos de Dados e Valores Nulos")
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
    df["Age"] = df["Subject's age"].apply(months_to_years)
    df.drop(columns=["Subject's age"], inplace=True)
    st.dataframe(df)
    df.to_csv(file_path, index=False)
    unique_subject_age = df["Age"].dropna().unique()
    st.write(unique_subject_age)
    df['Age'] = df['Age'].apply(remove_s)
    df['Age'] = df['Age'].apply(remove_variation)
    idade_especifica = '3 day'
    linha_idade_especifica = df.loc[df['Age'] == idade_especifica]
    st.write(linha_idade_especifica)
    df.to_csv(file_path, index=False)
    unique_subject_age = df["Age"].dropna().unique()
    st.write(unique_subject_age)
    st.dataframe(df)'''
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    median_age = df['Age'].median()
    df['Age'].fillna(median_age, inplace=True)
    df.to_csv(file_path, index=False)
if __name__ == "__main__":
    main()