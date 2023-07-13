import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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
    st.subheader('Valor absoluto de mortes separado por etnia')
    dataframe_fatal_encounters = pd.read_csv('data\\fatal_encounters_dot_org.csv')
    #Plotagem do histograma
    # Filtra o dataframe para uma raça específica
    fig1 = plt.figure()
    causa_especifica = selectBy(dataframe_fatal_encounters["Cause of death"])
    df_filtrado = dataframe_fatal_encounters[dataframe_fatal_encounters["Cause of death"] == causa_especifica]

    contagem = df_filtrado["Subject's race"].value_counts()

    contagem.plot(kind='bar')

    # Configurações do gráfico
    plt.xlabel('Causa da Morte')
    plt.ylabel('Contagem')

    # Exibe o gráfico
    st.pyplot(fig1)

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

    fig2 = plt.figure()
    selected_race_2 = selectBy(dataShootings['race'])
    df_filtrado_2 = dataShootings[dataShootings['race'] == selected_race_2]

    contagem_2 = df_filtrado_2["state"].value_counts()

    contagem_2.plot(kind='bar')

    # Configurações do gráfico
    plt.xlabel('Estado')
    plt.ylabel('Quantidade de mortes')

    # Exibe o gráfico
    st.pyplot(fig2)

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
    st.subheader('Relação entre uso de Body Camera e quantidade de mortes')
    fig, ax = plt.subplots()
    x_values = np.arange(2)  # Valores 0 e 1 no eixo x
    plt.bar(x_values, deaths_by_body_camera.values)
    plt.xticks(x_values, ['0', '1'])  # Define os rótulos do eixo x
    plt.xlabel('Body Camera')
    plt.ylabel('Quantidade de Mortes')
    st.pyplot(fig)

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

def runPlots():
    mapPlot()
    causeByRace()
    deathByState()
    raceByState()
    bodyCamera()
    boxPlotIdade()

runPlots()





    