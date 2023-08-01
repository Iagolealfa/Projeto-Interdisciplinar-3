import streamlit as st
import pandas as pd

def main():
    st.title('Resumo de Valores Nulos da Coluna "Unique ID"')

    file_path = "..\\data\\fatal_encounters_dot_org.csv"

    try:
        df = pd.read_csv(file_path)
        st.subheader('Resumo de Valores Nulos da Coluna "Unique ID":')

        num_null_values = df['Unique ID'].isnull().sum()

        total_rows = df.shape[0]  

        st.write(f"Total de linhas: {total_rows}")
        st.write(f"Número de linhas com 'Unique ID' nulo: {num_null_values}")

    except FileNotFoundError:
        st.error(f"Arquivo '{file_path}' não encontrado. Verifique o caminho e tente novamente.")

if __name__ == '__main__':
    main()
