import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title('Análise de Exploratória')

def selectBy(lista_itens):
    return st.selectbox('Selecione uma opção', lista_itens.unique())

def mapPlot():
    dataframe_fatal_encounters = pd.read_csv('data\\fatal_encounters_dot_org.csv')
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
    dataframe_fatal_encounters = pd.read_csv('data\\fatal_encounters_dot_org.csv')
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

def deathByState():
    dataShootings = pd.read_csv('data/shootings_wash_post.csv')

    st.subheader('Quantidade de mortes com separação de raça por estado')

    selected_race_2 = selectBy(dataShootings['race'])
    df_filtrado_2 = dataShootings[dataShootings['race'] == selected_race_2]

    contagem_2 = df_filtrado_2["state"].value_counts()

    fig = go.Figure(data=go.Bar(x=contagem_2.index, y=contagem_2))

    fig.update_layout(title='Quantidade de mortes com separação de raça por estado',
                    xaxis_title='Estado',
                    yaxis_title='Quantidade de mortes')

    # Exibe o gráfico usando o método st.plotly_chart()
    st.plotly_chart(fig)

    st.text(""" 
    Este gráfico apresenta a quantidade de mortes por estado, com cada uma das etnias 
    do conjunto de dados representada separadamente. Ele fornece informações semelhantes 
    ao mapa, mas de forma visualizada em um gráfico de barras. Através desse gráfico, 
    podemos obter uma ideia de quais etnias são mais afetadas por essas interações com a 
    polícia. Além disso, em conjunto com as informações extraídas do próximo gráfico, 
    que mostra a distribuição étnica total por estado, podemos identificar quais estados 
    estão mais suscetíveis a ocorrências de vítimas fatais nos encontros com a polícia.
    """)

def raceByState():
    dataShareRace = pd.read_csv('data/ShareRaceByCity.csv')
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

    st.text(""" 
    Este gráfico apresenta a distribuição étnica percentual entre todos os estados. Ele
    utiliza a porcentagem de cada etnia informada na base de dados e agrupa os dados por
    estado. Como mencionado anteriormente, em conjunto com o gráfico anterior, esse
    gráfico pode fornecer uma ideia de quais estados podem estar mais propensos a ter
    vítimas fatais em encontros com a polícia. No entanto, é importante ressaltar que
    alguns lugares podem apresentar valores superiores a 100% devido a erros nos
    dados.
    """)

def bodyCamera():
    dataShootings = pd.read_csv('data/shootings_wash_post.csv')
    filtered_data = dataShootings[['body_camera', 'manner_of_death']]
    filtered_data = filtered_data.dropna()
    deaths_by_body_camera = filtered_data.groupby('body_camera')['manner_of_death'].count()

    fig = go.Figure(data=go.Bar(x=deaths_by_body_camera.index, y=deaths_by_body_camera.values))

    fig.update_layout(title='Relação entre uso de Body Camera e quantidade de mortes',
                    xaxis_title='Body Camera',
                    yaxis_title='Quantidade de Mortes')

    st.plotly_chart(fig)

    st.text(""" 
    Este gráfico apresenta o total de mortes dividido entre ocorrências em que os
    policiais possuíam câmera em suas fardas e ocorrências em que não possuíam. 
    Pretendemos realizar uma correlação entre a presença ou ausência da câmera e a 
    possibilidade de ocorrer uma vítima fatal. Dessa forma, poderemos utilizar essa 
    variável como um dos fatores na predição.
    """)

def boxPlotIdade():
    dataset = pd.read_csv("data/shootings_wash_post.csv")
    st.subheader("Boxplot da Idade")
    idade = dataset["age"]
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=idade)
    plt.ylabel("Idade")
    plt.title("Boxplot da Idade")
    st.pyplot(plt)

    st.text(""" 
    Neste gráfico, é apresentada a média de idade das vítimas fatais em encontros com a
    polícia. Podemos utilizar essas informações para estabelecer uma correlação entre 
    faixas etárias que estão mais suscetíveis a essas ocorrências.
    """)

def plot_gender_and_weapon_counts():
    df = pd.read_csv("data/police_killings_MPV.csv")
    gender_counts = df["Victim's gender"].value_counts()
    weapon_counts = df["Unarmed/Did Not Have an Actual Weapon"].value_counts()
    gender_categories = ['Male', 'Female', 'Transgender', 'Unknown']
    weapon_categories = ['Allegedly Armed', 'Unarmed', 'Unclear', 'Vehicle']

    st.subheader("Gênero das vitimas")
    fig_gender = plt.figure(figsize=(10, 5))
    plt.bar(gender_categories, gender_counts)
    plt.xlabel("Gender")
    plt.ylabel("Count")
    st.pyplot(fig_gender)
    st.text(""" 
    O gráfico ilustra a quantidade de vítimas separadas por gênero. É possível notar uma 
    significativa disparidade no número de vítimas do sexo masculino em relação ao total.    
            """)

    st.subheader("Portando armas")
    fig_weapon = plt.figure(figsize=(10, 5))
    plt.bar(weapon_categories, weapon_counts)
    plt.xlabel("Weapon Status")
    plt.ylabel("Count")
    st.pyplot(fig_weapon)

    st.text(""" 
    
No gráfico, são apresentados os números de casos em que as vítimas estavam classific
adas em diferentes categorias: armada, desarmada, casos em que não ficou claro se a 
vítima possuía uma arma ou não, e quando a vítima utilizou um veículo como uma "arma".
    """)
def porcentagem_coluna():
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
def runPlots():
    mapPlot()
    causeByRace()
    deathByState()
    raceByState()
    bodyCamera()
    boxPlotIdade()
    plot_gender_and_weapon_counts()

runPlots()





    