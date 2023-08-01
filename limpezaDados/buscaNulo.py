import streamlit as st
import pandas as pd

def main():
    st.title('Tipos de Dados e Valores Nulos das Colunas do CSV')
    
    df = pd.read_csv('..\\data\\fatal_encounters_dot_org.csv')
    st.subheader('Tipos de Dados e Valores Nulos das Colunas:')
    
    data_types = df.dtypes

    has_null_values = df.isnull().any()

    info_df = pd.DataFrame({
            'Tipos de Dados': data_types,
            'Valores Nulos': has_null_values
        })

    st.write(info_df)



if __name__ == '__main__':
    main()
