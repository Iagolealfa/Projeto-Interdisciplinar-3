import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title = "Análise de Dados",
    
    menu_items = {
        'About': "TESTE DO ABOUT"
    }
)

st.title('Análise de Dados')


def selectBy(lista_itens):
    return st.selectbox('Selecione uma opção', lista_itens.unique())

#carregando a tabela fatal_encounters_dot_org
dataframe_fatal_encounters = pd.read_csv('..\data\\fatal_encounters_dot_org.csv')

#Ajustar colunas
dataframe_fatal_encounters.rename(columns={'Latitude': 'lat'}, inplace=True)
dataframe_fatal_encounters.rename(columns={'Longitude': 'lon'}, inplace=True)
dataframe_fatal_encounters['lat'] = dataframe_fatal_encounters['lat'].astype(float)
dataframe_fatal_encounters['lon'] = dataframe_fatal_encounters['lon'].astype(float)
dataframe_fatal_encounters['lat'].fillna(0, inplace=True)
dataframe_fatal_encounters['lon'].fillna(0, inplace=True)

dataframe_fatal_encounters["Subject's race"].fillna("Race unspecified", inplace=True)


#Plotagem do mapa
st.subheader('Mapa de distribuição de mortes')
selected_race = selectBy(dataframe_fatal_encounters["Subject's race"])

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

# Exibe o gráfico
st.pyplot(plt)

#Iago-------------------------------------------------------------------------------

dataShootings = pd.read_csv('../data/shootings_wash_post.csv')
st.subheader('Quantidade de mortes com separação de raça por estado')
grouped_data = dataShootings.groupby(['state', 'race']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Estado')
ax.set_ylabel('Quantidade')
ax.legend(title='Raça', title_fontsize='11', fontsize='9')
plt.tight_layout()
st.pyplot(fig)





dataShareRace = pd.read_csv('../data/ShareRaceByCity.csv')
dataShareRace = dataShareRace.replace('(X)', float('nan'))
dataShareRace['share_white'] = pd.to_numeric(dataShareRace['share_white'])
dataShareRace['share_black'] = pd.to_numeric(dataShareRace['share_black'])
dataShareRace['share_asian'] = pd.to_numeric(dataShareRace['share_asian'])
dataShareRace['share_native_american'] = pd.to_numeric(dataShareRace['share_native_american'])
dataShareRace['share_hispanic'] = pd.to_numeric(dataShareRace['share_hispanic'])
data_by_state = dataShareRace.groupby('Geographic area').mean()
st.subheader('Distribuição étnica por estado')
st.bar_chart(data_by_state)
plt.show()

filtered_data = dataShootings[['body_camera', 'manner_of_death']]
filtered_data = filtered_data.dropna()  
deaths_by_body_camera = filtered_data.groupby('body_camera')['manner_of_death'].count()
st.subheader('Relação entre uso de Body Camera e quantidade de mortes')
fig, ax = plt.subplots()
plt.bar(deaths_by_body_camera.index, deaths_by_body_camera.values)
plt.xlabel('Body Camera')
plt.ylabel('Quantidade de Mortes')
plt.title('Relação entre uso de Body Camera e quantidade de mortes')
st.pyplot(fig)



#Iago-------------------------------------------------------------------------------

def boxPlotIdade():
    st.subheader("Boxplot da Idade")
    dataset = pd.read_csv("../data/shootings_wash_post.csv")
    idade = dataset["age"]
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=idade)
    plt.ylabel("Idade")
    plt.title("Boxplot da Idade")
    st.pyplot(plt)



def main():
    boxPlotIdade()

if __name__ == "__main__":
    main()