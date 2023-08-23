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

def cluster_maker(dados, clusters_number):
    kmeans_dados = KMeans(n_clusters = clusters_number)
    kmeans_dados.fit(dados)

    centroides = kmeans_dados.cluster_centers_
    rotulos = kmeans_dados.labels_
    st.write(rotulos)

    if dados.shape[1] == 2:
       two_D_graph(dados, rotulos, centroides, clusters_number)
    elif dados.shape[1] > 2:
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

dados = pd.read_csv('data\\fatal_encounters_tratado.csv')
colunas=['Cause_of_death','Subjects_gender','Region','Subjects_race']
dados_categoricos = dados[colunas]
max_clusters = st.slider("Escolha o Número Máximo de Clusters para o Método do Cotovelo", min_value=1, max_value=10, value=10)
distortions = elbow_method_modes(dados_categoricos,max_clusters)
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_clusters + 1), distortions, marker='o')
plt.title("Método do Cotovelo")
plt.xlabel("Número de Clusters")
plt.ylabel("Distortion")
st.subheader("Gráfico do Método do Cotovelo")
st.pyplot(plt)


num_clusters = st.slider("Escolha o Número de Clusters", min_value=1, max_value=max_clusters, value=3)

clusters = k_modes_clustering(dados, num_clusters)
dados['Cluster'] = clusters

st.subheader("Conjunto de Dados com Resultados da Clusterização")
st.dataframe(dados)

plt.figure(figsize=(10, 6))
sns.countplot(x='Cluster', data=dados)
plt.title("Distribuição dos Clusters")
st.subheader("Gráfico da Distribuição dos Clusters")
st.pyplot(plt)