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


def check_nan(df):
    nan_columns = df.columns[df.isna().any()].tolist()
    if nan_columns:
        print("Colunas com valores NaN:")
        for col in nan_columns:
            nan_count = df[col].isna().sum()
            print(f"{col}: {nan_count} valores NaN")
    else:
        print("Nenhuma coluna possui valores NaN")
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

def remove_line(file_path):
    df = pd.read_csv(file_path)
    
    if "Subjects_name" in df.columns:
        df = df[df["Subjects_name"] != "This is a spacer for Fatal Encounters use."]
        df.to_csv(file_path, index=False)
        
def state_to_region(file_path):
    df = pd.read_csv(file_path)
    state_to_region = {
    'AL': 'Southeast',
    'AK': 'West',
    'AZ': 'Southwest',
    'AR': 'Southeast',
    'CA': 'West',
    'CO': 'West',
    'CT': 'Northeast',
    'DE': 'Northeast',
    'FL': 'Southeast',
    'GA': 'Southeast',
    'HI': 'West',
    'ID': 'West',
    'IL': 'Midwest',
    'IN': 'Midwest',
    'IA': 'Midwest',
    'KS': 'Midwest',
    'KY': 'Southeast',
    'LA': 'Southeast',
    'ME': 'Northeast',
    'MD': 'Northeast',
    'MA': 'Northeast',
    'MI': 'Midwest',
    'MN': 'Midwest',
    'MS': 'Southeast',
    'MO': 'Midwest',
    'MT': 'West',
    'NE': 'Midwest',
    'NV': 'West',
    'NH': 'Northeast',
    'NJ': 'Northeast',
    'NM': 'Southwest',
    'NY': 'Northeast',
    'NC': 'Southeast',
    'ND': 'Midwest',
    'OH': 'Midwest',
    'OK': 'Southwest',
    'OR': 'West',
    'PA': 'Northeast',
    'RI': 'Northeast',
    'SC': 'Southeast',
    'SD': 'Midwest',
    'TN': 'Southeast',
    'TX': 'Southwest',
    'UT': 'West',
    'VT': 'Northeast',
    'VA': 'Southeast',
    'WA': 'West',
    'WV': 'Southeast',
    'WI': 'Midwest',
    'WY': 'West'
}
    df["Region"] = df["Location_of_death_(state)"].map(state_to_region)
    df.to_csv(file_path, index=False)
def print_rows_with_nan(df):
    nan_rows = df[df.isna().any(axis=1)]
    if not nan_rows.empty:
        print("Linhas com valores NaN:")
        print(nan_rows)
    else:
        print("Nenhuma linha possui valores NaN")
def one_hot(coluna,prefix):
    df = pd.read_csv(file_path_new)
    df_enconded=pd.get_dummies(df, columns=[coluna],prefix=[prefix])
    df_enconded.to_csv(file_path_new, index=False)
def corrigir_linha():
    df=pd.read_csv(file_path_new)
    unique_value = "Tase"
    new_value='Tasered'
    df['Cause_of_death'] = df['Cause_of_death'].replace(unique_value, new_value)
    df.to_csv(file_path_new, index=False)
def fill_missing_with_mode(df):
    columns_with_missing = df.columns[df.isna().any()].tolist()
    for col in columns_with_missing:
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace=True)
    df.to_csv(file_path_new, index=False)        
def main():
    df1 = pd.read_csv(file_path)
    df2=pd.read_csv(file_path_new)
    fill_missing_with_mode(df2)
    check_nan(df2)
    print_rows_with_nan(df2)
    #add_coluna(file_path,file_path_new,'Cause_of_death') Comentado pois a coluna ja foi adcionada 
    #add_coluna(file_path,file_path_new,'Age') Comentado pois a coluna ja foi adcionada 
    #add_coluna(file_path,file_path_new,'Subjects_gender') Comentado pois a coluna ja foi adcionada 
    #add_imputation_control_column(file_path) Comentado pois a coluna ja foi adcionada com o valor nulo
    #imputar_race(file_path) Comentado pois ja foi substituido os Race unspecified por Subjects_race_with_imputations quando possivel
    #replace_unspecified_race_with_mode(file_path) Comentado pois já foi substituido os Race unspecified restantes pela moda
    #remove_line(file_path) Comentado pois a linha foi deletada
    #state_to_region(file_path)
    #add_coluna(file_path,file_path_new,"Region") Comentado pois a coluna já foi adcionada
    #add_coluna(file_path,file_path_new,"Subjects_race")
    #one_hot('Region','Region')
    #one_hot('Subjects_race','Race')
    #one_hot('Subjects_gender','Gender')
    #one_hot('Cause_of_death','Death')
    st.write(df2)

    #st.write(df2['Cause_of_death'].value_counts())

    st.write(df1.columns)
    
    st.write(valoresNulos(file_path,'Subjects_gender'))

    
    
    
    
    
if __name__ == '__main__':
    main()
