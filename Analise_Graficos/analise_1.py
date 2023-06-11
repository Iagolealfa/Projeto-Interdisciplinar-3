import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title = "Análise de Dados",
    layout = "wide",
    menu_items = {
        'About': "TESTE DO ABOUT"
    }
)

st.title('Análise de Dados')

data = pd.read_csv('../data/shootings_wash_post.csv')
st.write(data)
st.title('Quantidade de mortes com separação de raça por estado')
grouped_data = data.groupby(['state', 'race']).size().unstack(fill_value=0)


fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.plot(kind='bar', stacked=True, ax=ax)


ax.set_xlabel('Estado')
ax.set_ylabel('Quantidade')
ax.legend(title='Raça', title_fontsize='11', fontsize='9')


plt.tight_layout()


st.pyplot(fig)

#Neto---------------------------------------------------------------------------------------------------------------------------------------------------------
#Carrega a base de dados fatal_encounters_dot_org
dataframe_fatal_encounters = pd.read_csv('../data/fatal_encounters_dot_org.csv')

#Ajustar colunas
dataframe_fatal_encounters.rename(columns={'Latitude': 'LATITUDE'}, inplace=True)
dataframe_fatal_encounters.rename(columns={'Longitude': 'LONGITUDE'}, inplace=True)
dataframe_fatal_encounters['LATITUDE'] = dataframe_fatal_encounters['LATITUDE'].astype(float)
dataframe_fatal_encounters['LONGITUDE'] = dataframe_fatal_encounters['LONGITUDE'].astype(float)
dataframe_fatal_encounters['LATITUDE'].fillna(0, inplace=True)
dataframe_fatal_encounters['LONGITUDE'].fillna(0, inplace=True)

dataframe_fatal_encounters["Subject's race"].fillna("Race unspecified", inplace=True)


#Plotagem do mapa
selected_race = st.selectbox('Selecione uma opção', dataframe_fatal_encounters["Subject's race"].unique())

st.map(dataframe_fatal_encounters[dataframe_fatal_encounters["Subject's race"] == selected_race])


#Plotagem do histograma
# Filtra o dataframe para uma raça específica
causa_especifica = st.selectbox('Selecione uma opção', dataframe_fatal_encounters["Cause of death"].unique())
st.subheader('Valor absoluto de mortes separado por etnia')
df_filtrado = dataframe_fatal_encounters[dataframe_fatal_encounters["Cause of death"] == causa_especifica]

contagem = df_filtrado["Subject's race"].value_counts()

st.bar_chart(contagem)

contagem.plot(kind='bar')

# Configurações do gráfico
plt.xlabel('Causa da Morte')
plt.ylabel('Contagem')
plt.title(f'Valor absoluto separado por raça de mortes por: {causa_especifica}')

# Exibe o gráfico
st.pyplot(plt)
#Neto---------------------------------------------------------------------------------------------------------------------------------------------------------