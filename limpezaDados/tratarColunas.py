import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "..\\data\\fatal_encounters_dot_org_updated_1.csv"
file_path_new = "..\\data\\fatal_encounters_tratado.csv"

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
    
def valoresNulos(file_path,name_coluna):
    
    st.title('Resumo de Valores Nulos da Coluna')
    
    df = pd.read_csv(file_path)
    st.subheader('Resumo de Valores Nulos da Coluna:')

    num_null_values = df[name_coluna].isnull().sum()
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
    df.loc[mask, 'imputation_control'] = True  

    df.to_csv(file_path, index=False)



def drop_colunas(file_path,name_coluna):
    df = pd.read_csv(file_path)
    colunas_para_apagar = [name_coluna]
    df = df.drop(columns=colunas_para_apagar)

    df.to_csv(file_path, index=False)

def coluna_others(file_path,name_coluna):
    df = pd.read_csv(file_path)
    df[name_coluna] = df[name_coluna].apply(lambda x: x if x in ['Gunshot', 'Vehicle', 'Tasered'] else 'Others')
    df[name_coluna].to_csv("..\\data\\fatal_encounters_tratado.csv", index=False)

def add_coluna(file_path,file_path_new,name_coluna):
    df1 = pd.read_csv(file_path)
    df2= pd.read_csv(file_path_new)
    df2[name_coluna] = df1[name_coluna]
    df2.to_csv("..\\data\\fatal_encounters_tratado.csv", index=False)    

def add_imputation_control_column(file_path):
    df = pd.read_csv(file_path)
    df["imputation_control"] = False
    df.to_csv(file_path, index=False)

def replace_unspecified_race_with_mode(file_path):
    df = pd.read_csv(file_path)
    mode_value = df['Subjects_race'].mode().iloc[0]
    df.loc[df['Subjects_race'] == 'Race unspecified', 'Subjects_race'] = mode_value
    df.to_csv(file_path, index=False)



def main():
    df1 = pd.read_csv(file_path)
    df2=pd.read_csv(file_path_new)
    
    #add_coluna(file_path,file_path_new,'Cause_of_death') Comentado pois a coluna ja foi adcionada 
    #add_coluna(file_path,file_path_new,'Age') Comentado pois a coluna ja foi adcionada 
    #add_coluna(file_path,file_path_new,'Subjects_gender') Comentado pois a coluna ja foi adcionada 
    #add_imputation_control_column(file_path) Comentado pois a coluna ja foi adcionada com o valor nulo
    #imputar_race(file_path) Comentado pois ja foi substituido os Race unspecified por Subjects_race_with_imputations quando possivel
    #replace_unspecified_race_with_mode(file_path) Comentado pois já foi substituido os Race unspecified restantes pela moda

    st.write(df1['Subjects_gender'].value_counts())

    st.write(df1.columns)
    
    st.write(valoresNulos(file_path,'Subjects_gender'))

    
    
    
    
    
if __name__ == '__main__':
    main()
