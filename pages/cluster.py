import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA


def data_scaler(dados):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dados)
    return scaled_data

def elbow_method(dados):
    dados = data_scaler(dados)
    wcss = []
    clusters_number = 0
    for i in range(1, 11):
        kmeans_cartao = KMeans(n_clusters=i, random_state=0)
        kmeans_cartao.fit(dados)
        wcss.append(kmeans_cartao.inertia_)
    elbow_graph = px.line(x = range(1,11), y = wcss)
    st.plotly_chart(elbow_graph)

def cluster(dados, clusters_number):
    dados = data_scaler(dados)

    kmeans_dados = KMeans(n_clusters = clusters_number)
    kmeans_dados.fit(dados)

    centroides = kmeans_dados.cluster_centers_
    rotulos = kmeans_dados.labels_

    if dados.shape[1] == 2:
       two_D_graph(dados, rotulos, centroides, clusters_number)
    elif dados.shape[1] > 2:
        mult_D_graph(dados, rotulos, centroides, clusters_number)

def two_D_graph(dados, rotulos, centroides, clusters_number):
    centroids_size = []
    for i in range(clusters_number):
        centroids_size.append(3)
    two_D_graph_1 = px.scatter(x = dados[:,0], y = dados[:,1], color=rotulos)
    two_D_graph_2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = centroids_size)
    two_D_graph_3 = go.Figure(data = two_D_graph_1.data + two_D_graph_2.data)
    st.plotly_chart(two_D_graph_3)

def mult_D_graph(dados, rotulos, centroides, clusters_number):
    centroids_size = []
    for i in range(clusters_number):
        centroids_size.append(3)
    pca = PCA(n_components=2)
    dados_pca = pca.fit_transform(dados)
    dados_pca.shape
    dados_pca
    mult_D_graph_1 = px.scatter(x= dados_pca[:,0], y = dados_pca[:,1], color=rotulos)
    mult_D_graph_2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = centroids_size)
    mult_D_graph_3 = go.Figure(data = mult_D_graph_1.data + mult_D_graph_2.data)
    st.plotly_chart(mult_D_graph_3)


# X_random, y_random = make_blobs(n_samples=200, centers=5, random_state=1)
# X_random
# y_random
# grafico = px.scatter(x = X_random[:,0], y = X_random[:,1])
# st.plotly_chart(grafico)
# kmeans_blobs = KMeans(n_clusters=5)
# kmeans_blobs.fit(X_random)
# rotulos = kmeans_blobs.predict(X_random)
# rotulos
# centroides = kmeans_blobs.cluster_centers_
# centroidescentroides = kmeans_blobs.cluster_centers_
# centroides
# X_random.lenght()
# grafico1 = px.scatter(x = X_random[:,0], y = X_random[:,1], color = rotulos)
# grafico2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = [5, 5, 5, 5, 5])
# grafico3 = go.Figure(data = grafico1.data + grafico2.data)
# st.plotly_chart(grafico3)