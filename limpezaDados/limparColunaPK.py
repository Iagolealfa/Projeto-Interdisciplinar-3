import streamlit as st
import pandas as pd

file_path = "..\\data\\police_killings_MPV.csv"

def ler_dataset_e_contar_valores(file_path, colunas):
    df = pd.read_csv(file_path)
    resultados = {}

    for coluna in colunas:
        valores_unicos = df[coluna].unique()
        contagem_valores = df[coluna].value_counts()
        valores_nulos = df[coluna].isna().sum()  # Conta valores nulos
        resultados[coluna] = {
            'Valores Únicos': valores_unicos,
            'Contagem de Valores': contagem_valores,
            'Valores Nulos': valores_nulos  # Adiciona a contagem de valores nulos
        }

    return resultados

def main():
    st.title("Contagem de Valores em um Dataset")
   
    colunas = ["Symptoms of mental illness", "Unarmed/Did Not Have an Actual Weapon", "Alleged Weapon", "Fleeing", "Body Camera"]
    if st.button("Contar Valores"):

        resultados = ler_dataset_e_contar_valores(file_path, colunas)
        for coluna, resultado in resultados.items():
            st.write(f"Coluna: {coluna}")
            
            st.write("Contagem de Valores:")
            st.write(resultado['Contagem de Valores'])
            st.write("Valores Nulos:")
            st.write(resultado['Valores Nulos'])

#tratar Symptoms of mental illness
def Mental_illnessUnknown(file_path):
    df = pd.read_csv(file_path)
    df['Symptoms of mental illness'] = df['Symptoms of mental illness'].str.replace(r'Unkown|unknown', 'Unknown', case=False)
    df.to_csv(file_path, index=False)

def substituir_valores_nulos(file_path):
    df = pd.read_csv(file_path)
    df['Symptoms of mental illness'].fillna('Unknown', inplace=True)
    df.to_csv(file_path, index=False)

#tratar Alleged Weapon
def AgruparWeapon(file_path):
    df = pd.read_csv(file_path)
    top_values = df['Alleged Weapon'].value_counts().nlargest(6).index.tolist()
    df.loc[~df['Alleged Weapon'].isin(top_values), 'Alleged Weapon'] = 'others'
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    main()
    AgruparWeapon(file_path)
    Mental_illnessUnknown(file_path)
    substituir_valores_nulos(file_path)