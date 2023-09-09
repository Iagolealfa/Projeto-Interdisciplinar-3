import streamlit as st
import pandas as pd

file_path = "..\\data\\police_killings_MPV.csv"

def ler_dataset_e_contar_valores(file_path, colunas):
    df = pd.read_csv(file_path)
    resultados = {}

    for coluna in colunas:
        valores_unicos = df[coluna].unique()
        contagem_valores = df[coluna].value_counts()
        valores_nulos = df[coluna].isna().sum() 
        resultados[coluna] = {
            'Valores Únicos': valores_unicos,
            'Contagem de Valores': contagem_valores,
            'Valores Nulos': valores_nulos  
        }

    return resultados

def main():
    st.title("Contagem de Valores em um Dataset")
   
    colunas = ["Symptoms of mental illness", "Unarmed/Did Not Have an Actual Weapon", "Alleged Weapon", "Fleeing", "Body Camera","Victims gender","Victims race"]
    if st.button("Contar Valores"):

        resultados = ler_dataset_e_contar_valores(file_path, colunas)
        for coluna, resultado in resultados.items():
            st.write(f"Coluna: {coluna}")
            
            st.write("Contagem de Valores:")
            st.write(resultado['Contagem de Valores'])
            st.write("Valores Nulos:")
            st.write(resultado['Valores Nulos'])


def substituir_valores_nulos(file_path):
    df = pd.read_csv(file_path)
    df['Symptoms of mental illness'].fillna('Unknown', inplace=True)
    df.to_csv(file_path, index=False)

def AgruparWeapon(file_path):
    df = pd.read_csv(file_path)
    top_values = df['Alleged Weapon'].value_counts().nlargest(6).index.tolist()
    df.loc[~df['Alleged Weapon'].isin(top_values), 'Alleged Weapon'] = 'others'
    df.to_csv(file_path, index=False)


def correcaoCase(file_path,coluna,nomeOut,nomeIn):
    df = pd.read_csv(file_path)
    df[coluna] = df[coluna].str.replace(nomeOut, nomeIn, case=False)
    df.to_csv(file_path, index=False)

def nuloModa(file_path,coluna):
    df = pd.read_csv(file_path)
    df[coluna].fillna(df[coluna].mode()[0], inplace=True)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    main()
    AgruparWeapon(file_path)
    substituir_valores_nulos(file_path)
    correcaoCase(file_path=file_path,coluna='Symptoms of mental illness',nomeOut='Unkown',nomeIn='Unknown')
    correcaoCase(file_path=file_path,coluna='Symptoms of mental illness',nomeOut='unknown',nomeIn='Unknown')
    correcaoCase(file_path=file_path,coluna='Fleeing',nomeOut='car',nomeIn='Car')
    correcaoCase(file_path=file_path,coluna='Fleeing',nomeOut='foot',nomeIn='Foot')
    correcaoCase(file_path=file_path,coluna='Fleeing',nomeOut='not fleeing',nomeIn='Not fleeing')
    correcaoCase(file_path=file_path,coluna='Body Camera',nomeOut='no',nomeIn='No')
    correcaoCase(file_path=file_path,coluna='Body Camera',nomeOut='Bystander Video',nomeIn='Yes')
    correcaoCase(file_path=file_path,coluna='Body Camera',nomeOut='Surveillance Video',nomeIn='Yes')
    nuloModa(file_path=file_path,coluna='Victims gender')
