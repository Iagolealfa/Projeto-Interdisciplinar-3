import streamlit as st
import pandas as pd

file_path = "..\\data\\fatal_encounters_dot_org_updated_2.csv"

def remove_variation(age_str):
    try:
        return age_str.replace('3 day', '0.0082')
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
    
def valoresNulos(file_path):
    
    st.title('Resumo de Valores Nulos da Coluna')
    
    df = pd.read_csv(file_path)
    st.subheader('Resumo de Valores Nulos da Coluna:')

    num_null_values = df['Subjects_gender'].isnull().sum()
    total_rows = df.shape[0]  

    st.write(f"Total de linhas: {total_rows}")
    st.write(f"Número de nulo na coluna: {num_null_values}")

def ler_e_renomear_colunas(file_path):
    df = pd.read_csv(file_path)


    df.columns = df.columns.str.replace("'", "")


    df.columns = df.columns.str.replace(' ', '_')

    df.rename(columns=lambda x: x.strip().replace("'", "").replace(" ", "_"), inplace=True)
    df.to_csv(file_path, index=False)

    return df



def deletar_linha_por_valor(file_path, column_name, value):
    df = pd.read_csv(file_path)

    df = df[df[column_name] != value]

    
    st.dataframe(df)



def imputar_race(file_path):
    df = pd.read_csv(file_path)

    mask = (df['Subjects_race'] == 'Race unspecified') & (df['Subjects_race_with_imputations'].notnull())
    df.loc[mask, 'Subjects_race'] = df.loc[mask, 'Subjects_race_with_imputations']

    df.to_csv(file_path, index=False)


def drop_colunas(file_path):
    df = pd.read_csv(file_path)
    colunas_para_apagar = ['Date_(Year)']
    df = df.drop(columns=colunas_para_apagar)

    df.to_csv(file_path, index=False)

def main():
    df = pd.read_csv(file_path)
    st.write(df.columns)
    one_hot_encoded = pd.get_dummies(df, columns=['Subjects_gender'], prefix=['Gender'])
    one_hot_encoded.to_csv(file_path, index=False)
    #df.to_csv(file_path, index=False)
    st.write(one_hot_encoded )
    
    
    
if __name__ == '__main__':
    main()
