import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from kmodes.kmodes import KModes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt


def data_scaler(dados):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dados)
    return scaled_data

def elbow_method(dados):
    wcss = []
    clusters_number = 0
    for i in range(1, 8):
        kmeans_cartao = KMeans(n_clusters=i, random_state=0)
        kmeans_cartao.fit(dados)
        wcss.append(kmeans_cartao.inertia_)
    elbow_graph = px.line(x = range(1,8), y = wcss)
    st.plotly_chart(elbow_graph)

def k_means_clustering(dados, clusters_number, dimension_reducer):
    kmeans_dados = KMeans(n_clusters = clusters_number)
    kmeans_dados.fit(dados)

    centroides = kmeans_dados.cluster_centers_
    rotulos = kmeans_dados.labels_

    if dados.shape[1] == 2:
       two_D_graph(dados, rotulos, centroides, clusters_number)
    elif dados.shape[1] > 2 and dimension_reducer == 'pca':
        dimension_reducer_pca(dados, rotulos, clusters_number)
    else:
       dimension_reducer_tsne(dados, rotulos, clusters_number)

def two_D_graph(dados, rotulos, centroides, clusters_number):
    centroids_size = []
    for i in range(clusters_number):
        centroids_size.append(3)
    two_D_graph_1 = px.scatter(x = dados[:,0], y = dados[:,1], color=rotulos)
    two_D_graph_2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = centroids_size)
    two_D_graph_3 = go.Figure(data = two_D_graph_1.data + two_D_graph_2.data)
    st.plotly_chart(two_D_graph_3)

def dimension_reducer_pca(dados, rotulos, clusters_number):
    pca = PCA(n_components=2)
    dados_pca = pca.fit_transform(dados)
    mult_D_graph = px.scatter(x= dados_pca[:,0], y = dados_pca[:,1], color=rotulos)
    st.plotly_chart(mult_D_graph)

def dimension_reducer_tsne(dados, rotulos, clusters_number):
    tsne = TSNE(n_components=2, random_state=0)
    data_transformed = tsne.fit_transform(dados)
    mult_D_graph = px.scatter(x= data_transformed[:,0], y = data_transformed[:,1], color=rotulos)
    st.plotly_chart(mult_D_graph)

def elbow_method_modes(data, max_clusters):
    distortions = []
    for n_clusters in range(1, max_clusters + 1):
        kmodes = KModes(n_clusters=n_clusters, init='Huang', n_init=10, verbose=0)
        kmodes.fit(data)
        distortions.append(kmodes.cost_)
    return distortions

def k_modes_clustering(data, num_clusters):
    kmodes = KModes(n_clusters=num_clusters, init='Huang', n_init=10, verbose=0)
    clusters = kmodes.fit_predict(data)
    return clusters

st.title('Clusters')
st.subheader('K-maens')
st.text('''
    Quando começamos a parte de clusterização acabamos optando pela utilização do k-means, para poder aplicar o k-means criamos 
    algumas funções, as primeiras foram o data_scaler com a função de normalizar os dados, para nenhum se sobre sair em relação
    a outro por conta de um valor mais alto e o elbow_method, que utiliza o metodo do cotovelo para determinar a quantidade ideal
    de cluster para os nossos dados.
''')

dados_one_hot = pd.read_csv('data/fatal_encounters_one_hot_encoding.csv')
dados_one_hot = dados_one_hot.values
dados_one_hot = data_scaler(dados_one_hot)
elbow_method(dados_one_hot)

st.text('''
    Também implementamos a k_means_clustering junto a mais duas funções: two_D_graph e mult_D_graph
    que juntas clusterizavam os dados e plotavam um gráfico de distribuição ou 2D para quando se tinha apenas duas dimensões ou
    o multiD que utilizava PCA para reduzir as dimensões dos dados para 2 para poder plotar um gráfico de distribuição.
''')
 
k_means_clustering(dados_one_hot, 4, 'pca')

st.text('''
    Porém achamos que a distribuição e a visualização do gráfico de disperção havia ficado um pouco estranha, e pesquisando mais
    descobrimos que o pca não é o ideal para reduzir as dimensionalidades nesse caso, onde temos todos os dados categoricos, nesse
    caso o mais ideal seria o tsne, que é outro metodo com o mesmo fim. Além disso, também decidimo por tirar o data_scaler, pois
    não havia sentido em escalonar dados que são todos binarios e isso podia também estar afetando o resultado dos clusters e a 
    visaualização do gráfico.
''')

dados_one_hot = pd.read_csv('data/fatal_encounters_one_hot_encoding.csv')
dados_one_hot = dados_one_hot.values
k_means_clustering(dados_one_hot, 4, 'tsne')

st.text('''
    Mas pesquisando um pouco mais afundo, descobrimos que o ideal para dados que possuem muitos valores categorigos, como no nosso
    onde todos são categoricos, com exceção da idade, o ideal seria utilizar o K-modes, que é uma variação do K-mean, porém como o
    nome diz, ao enves de utilizar média, utiliza moda.
''')


st.subheader('K-modes')
dados = pd.read_csv('data\\fatal_encounters_tratado.csv')
st.text('''
    A partir disso fizemos uma função para aplicar o método d cotovelo nos dados utilizando k-modes para podermos saber o número
    ideal de clusters.
''')
max_clusters = st.slider("Escolha o Número Máximo de Clusters para o Método do Cotovelo", min_value=1, max_value=10, value=10)
# distortions = elbow_method_modes(dados,max_clusters)
# plt.figure(figsize=(10, 6))
# plt.plot(range(1, max_clusters + 1), distortions, marker='o')
# plt.title("Método do Cotovelo")
# plt.xlabel("Número de Clusters")
# plt.ylabel("Distortion")
# st.subheader("Gráfico do Método do Cotovelo")
# st.pyplot(plt)

st.text('''
    Então fizemos uma função que gera os clusters utilizando o k-modes. Então geramso um gráfico de barra que mostra a distribuição 
    de cada cluster. Não fizemos um gráfico de distribuição, que normalmente é o melhor tipo de visualização para clusters
    porque, no k-modes os dados são mantidos como categorigos e não transformados em dados binarios utilizando o one hot encoding.
''')

num_clusters = st.slider("Escolha o Número de Clusters", min_value=1, max_value=max_clusters, value=3)
clusters = k_modes_clustering(dados, 4)
dados['Cluster'] = clusters

plt.figure(figsize=(10, 6))
sns.countplot(x='Cluster', data=dados)
plt.title("Distribuição dos Clusters")
st.subheader("Gráfico da Distribuição dos Clusters")
st.pyplot(plt)


