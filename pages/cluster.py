import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
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
    for i in range(1, 31):
        kmeans_cartao = KMeans(n_clusters=i, random_state=0)
        kmeans_cartao.fit(dados)
        wcss.append(kmeans_cartao.inertia_)
    elbow_graph = px.line(x = range(1,31), y = wcss)
    st.plotly_chart(elbow_graph)

def cluster_maker(dados, clusters_number):
    dados = data_scaler(dados)

    kmeans_dados = KMeans(n_clusters = clusters_number)
    kmeans_dados.fit(dados)

    centroides = kmeans_dados.cluster_centers_
    rotulos = kmeans_dados.labels_
    st.write(rotulos)

    if dados.shape[1] == 2:
       two_D_graph(dados, rotulos, centroides, clusters_number)
    elif dados.shape[1] > 2:
        mult_D_graph(dados, rotulos, clusters_number)

def two_D_graph(dados, rotulos, centroides, clusters_number):
    centroids_size = []
    for i in range(clusters_number):
        centroids_size.append(3)
    two_D_graph_1 = px.scatter(x = dados[:,0], y = dados[:,1], color=rotulos)
    two_D_graph_2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = centroids_size)
    two_D_graph_3 = go.Figure(data = two_D_graph_1.data + two_D_graph_2.data)
    st.plotly_chart(two_D_graph_3)

def mult_D_graph(dados, rotulos, clusters_number):
    pca = PCA(n_components=2)
    dados_pca = pca.fit_transform(dados)
    mult_D_graph = px.scatter(x= dados_pca[:,0], y = dados_pca[:,1], color=rotulos)
    st.plotly_chart(mult_D_graph)


dados = pd.read_csv('data\\fatal_encounters_dot_org_updated_2.csv')
dados = dados.values
st.write(dados)
dados = dados[:, 5:]

st.write(dados)
elbow_method(dados)

cluster_maker(dados, 22)

