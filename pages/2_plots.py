import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

st.title('Análise de Exploratória')

def selectBy(lista_itens):
    return st.selectbox('Selecione uma opção', lista_itens.unique())

def mapPlot():
    dataframe_fatal_encounters = pd.read_csv('dataframeSujo\\fatal_encounters_dot_org.csv')
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

    st.text("""
    Mapa mostrando a distribuição de mortes por etnia utilizando os dados de latitude
    e longitude encontrados na tabela "fatal_encounters_dot_org". Essa visualização 
    pode nos fornecer informações sobre as regiões do país onde ocorrem mais mortes
    para cada uma das etnias presentes no conjunto de dados. Pretendemos utilizar essas
    informações juntamente com indicadores demográficos para investigar se regiões com
    maior índice de pobreza ou menor nível de escolaridade, por exemplo, apresentam um
    maior número de vítimas fatais em encontros com a polícia.
    """)

def causeByRace():
    dataframe_fatal_encounters = pd.read_csv('dataframeSujo\\fatal_encounters_dot_org.csv')
    #Plotagem do histograma
    # Filtra o dataframe para uma raça específica
    
    causa_especifica = selectBy(dataframe_fatal_encounters["Cause of death"])
    df_filtrado = dataframe_fatal_encounters[dataframe_fatal_encounters["Cause of death"] == causa_especifica]

    contagem = df_filtrado["Subject's race"].value_counts()

    fig1 = go.Figure(data=go.Bar(x=contagem.index, y=contagem))

    fig1.update_layout(title = 'Valor absoluto de mortes separado por etnia',
                       xaxis_title='Causa da Morte',
                       yaxis_title='Contagem')
    st.plotly_chart(fig1)

    st.text(""" 
    Este gráfico apresenta a quantidade de mortes registradas para cada uma das causas, 
    como gunshot (arma de fogo), vehicle (veículo) e asphyxiated (asfixia), divididas 
    por etnia no conjunto de dados. O objetivo desse gráfico é visualizar qual causa 
    tem maior incidência em cada etnia e identificar qual etnia é mais afetada por cada 
    causa, permitindo uma correlação entre a distribuição étnica nas regiões do país e 
    o número de vítimas fatais em encontros com a polícia.
    """)




def plot_gender_and_weapon_counts():
    df = pd.read_csv("data/police_killings_MPV.csv")
    gender_counts = df["Victim's gender"].value_counts()
    weapon_counts = df["Unarmed/Did Not Have an Actual Weapon"].value_counts()
    gender_categories = ['Male', 'Female', 'Transgender', 'Unknown']
    weapon_categories = ['Allegedly Armed', 'Unarmed', 'Unclear', 'Vehicle']

    st.subheader("Gênero das vítimas")
    fig_gender = px.bar(x=gender_categories, y=gender_counts, labels={'x': 'Gênero', 'y': 'Contagem'})
    st.plotly_chart(fig_gender)
    st.text(""" 
    O gráfico ilustra a quantidade de vítimas separadas por gênero. É possível notar uma 
    significativa disparidade no número de vítimas do sexo masculino em relação ao total.    
    """)

    st.subheader("Portando armas")
    fig_weapon = px.bar(x=weapon_categories, y=weapon_counts, labels={'x': 'Status da Arma', 'y': 'Contagem'})
    st.plotly_chart(fig_weapon)
    st.text(""" 
    No gráfico, são apresentados os números de casos em que as vítimas estavam classificadas
    em diferentes categorias: armada, desarmada, casos em que não ficou claro se a vítima possuía uma arma,
    e casos envolvendo veículos.
    """)
def porcentagem_coluna():
    df = pd.read_csv('data/fatal_encounters_dot_org_updated_1.csv')
    contagem_valores = df['Cause_of_death'].value_counts()
    
    porcentagens = (contagem_valores / contagem_valores.sum()) * 100

    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=porcentagens.index, y=porcentagens.values)
    plt.xticks(rotation=45)
    plt.xlabel('Causa de Morte')
    plt.ylabel('Porcentagem')
    plt.title('Porcentagens das Causas de Morte')

    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    
    st.write("Tabela de Contagem e Porcentagens:")
    st.write(pd.DataFrame({'Causa de Morte': contagem_valores.index, 'Contagem': contagem_valores, 'Porcentagem (%)': porcentagens}))

def plot_race_by_region():
    df = pd.read_csv('data/fatal_encounters_tratado.csv')
    
    
    grouped_data = df.groupby(['Subjects_race', 'Region']).size().reset_index(name='Count')
    
    
    fig = px.bar(grouped_data, x='Region', y='Count', color='Subjects_race',
                 labels={'Region': 'Região', 'Count': 'Contagem', 'Subjects_race': 'Raça'})
    
    fig.update_layout(title="Quantidade de cada Raça por Região",
                      xaxis_title="Região",
                      yaxis_title="Contagem",
                      legend_title="Raça")
    
    st.plotly_chart(fig)    
    st.text(""" 
     Este gráfico apresenta a distribuição étnica percentual entre todos as regiões. Ele
     utiliza a porcentagem de cada etnia informada na base de dados e agrupa os dados por
     estado. Como mencionado anteriormente, em conjunto com o gráfico anterior, esse
     gráfico pode fornecer uma ideia de quais regiões podem estar mais propensos a ter
     vítimas fatais em encontros com a polícia. 
     """)
def runPlots():
    mapPlot()
    causeByRace()
    plot_gender_and_weapon_counts()
    plot_race_by_region()

runPlots()





    