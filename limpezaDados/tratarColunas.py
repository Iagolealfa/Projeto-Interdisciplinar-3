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

    num_null_values = df['Subjects_race'].isnull().sum()
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
    colunas_para_apagar = ['Imputation_probability','URL_of_image_of_deceased','Date_of_injury_resulting_in_death_(month/day/year)','Location_of_injury_(address)','Location_of_death_(zip_code)','Location_of_death_(county)','Full_Address','Latitude','Longitude','Agency_responsible_for_death','A_brief_description_of_the_circumstances_surrounding_the_death','Intentional_Use_of_Force_(Developing)','Symptoms_of_mental_illness?_INTERNAL_USE','_NOT_FOR_ANALYSIS.1','Video','Date&Description','Unique_ID_formula','Unique_identifier_(redundant)']
    df = df.drop(columns=colunas_para_apagar)

    df.to_csv(file_path, index=False)

def main():
    drop_colunas(file_path)
    imputar_race(file_path)
    df = pd.read_csv(file_path) 
    st.write(df.columns)
    
    
    
if __name__ == '__main__':
    main()
