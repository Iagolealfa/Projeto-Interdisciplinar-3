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
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.cm as cm

def cluster_and_silhouette(dados, n_clusters):
    km = KModes(n_clusters=n_clusters, init='Huang', n_init=10, verbose=0)
    clusters = km.fit_predict(dados)
    silhouette_avg = silhouette_score(dados, clusters, metric='hamming')
    return clusters, silhouette_avg
def plot_silhouette(silhouette_avg, silhouette_values, clusters):
    fig, ax = plt.subplots()
    y_lower = 10
    for i in range(clusters):
        ith_cluster_silhouette_values = silhouette_values[clusters == i]
        ith_cluster_silhouette_values.sort()
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
        color = cm.nipy_spectral(float(i) / clusters)
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)
        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax.set_yticks([])
    ax.set_xlabel("Valores de Silhueta")
    ax.set_ylabel("Rótulos dos Clusters")
    ax.set_title("Gráfico da Silhueta")
    st.pyplot(fig)
def dados_scaler(dados):
    scaler = StandardScaler()
    scaled_dados = scaler.fit_transform(dados)
    return scaled_dados

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
    two_D_graph_3 = go.Figure(dados = two_D_graph_1.dados + two_D_graph_2.dados)
    st.plotly_chart(two_D_graph_3)

def dimension_reducer_pca(dados, rotulos, clusters_number):
    pca = PCA(n_components=2)
    dados_pca = pca.fit_transform(dados)
    mult_D_graph = px.scatter(x= dados_pca[:,0], y = dados_pca[:,1], color=rotulos)
    st.plotly_chart(mult_D_graph)

def dimension_reducer_tsne(dados, rotulos, clusters_number):
    tsne = TSNE(n_components=2, random_state=0)
    dados_transformed = tsne.fit_transform(dados)
    mult_D_graph = px.scatter(x= dados_transformed[:,0], y = dados_transformed[:,1], color=rotulos)
    st.plotly_chart(mult_D_graph)

def elbow_method_modes(dados, max_clusters):
    distortions = []
    for n_clusters in range(1, max_clusters + 1):
        kmodes = KModes(n_clusters=n_clusters, init='Huang', n_init=10, verbose=0)
        kmodes.fit(dados)
        distortions.append(kmodes.cost_)
    return distortions

def k_modes_clustering(dados, num_clusters):
    kmodes = KModes(n_clusters=num_clusters, init='Huang', n_init=10, verbose=0)
    clusters = kmodes.fit_predict(dados)
    return clusters
def distribuicao_Cluster(dados):
    cluster_counts = dados['Cluster'].value_counts()

    
    colors = ['rgb(131, 201, 255)', 'rgb(0, 104, 201)', 'rgb(255, 171, 171)', 'rgb(255, 43, 43)','rgb(41,176,157)','rgb(80,0,80)','rgb(255,255,0)']

    
    fig = go.Figure(data=go.Bar(
        x=cluster_counts.index,
        y=cluster_counts.values,
        marker_color=colors
    ))
    fig.update_layout(
        title="Distribuição dos Clusters",
        xaxis_title="Clusters",
        yaxis_title="Contagem",
        xaxis=dict(type='category'),
        showlegend=False
    )

    
    st.subheader("Gráfico da Distribuição dos Clusters")
    st.plotly_chart(fig)
# st.title('Clusters')
# st.subheader('K-maens')
# st.text('''
#     Quando começamos a parte de clusterização acabamos optando pela utilização do k-means, para poder aplicar o k-means criamos 
#     algumas funções, as primeiras foram o dados_scaler com a função de normalizar os dados, para nenhum se sobre sair em relação
#     a outro por conta de um valor mais alto e o elbow_method, que utiliza o metodo do cotovelo para determinar a quantidade ideal
#     de cluster para os nossos dados.
# ''')

# dados_one_hot = pd.read_csv('dados/fatal_encounters_one_hot_encoding.csv')
# dados_one_hot = dados_one_hot.values
# dados_one_hot = dados_scaler(dados_one_hot)
# elbow_method(dados_one_hot)

# st.text('''
#     Também implementamos a k_means_clustering junto a mais duas funções: two_D_graph e mult_D_graph
#     que juntas clusterizavam os dados e plotavam um gráfico de distribuição ou 2D para quando se tinha apenas duas dimensões ou
#     o multiD que utilizava PCA para reduzir as dimensões dos dados para 2 para poder plotar um gráfico de distribuição.
# ''')
 
# k_means_clustering(dados_one_hot, 4, 'pca')

# st.text('''
#     Porém achamos que a distribuição e a visualização do gráfico de disperção havia ficado um pouco estranha, e pesquisando mais
#     descobrimos que o pca não é o ideal para reduzir as dimensionalidades nesse caso, onde temos todos os dados categoricos, nesse
#     caso o mais ideal seria o tsne, que é outro metodo com o mesmo fim. Além disso, também decidimo por tirar o dados_scaler, pois
#     não havia sentido em escalonar dados que são todos binarios e isso podia também estar afetando o resultado dos clusters e a 
#     visaualização do gráfico.
# ''')

# dados_one_hot = pd.read_csv('dados/fatal_encounters_one_hot_encoding.csv')
# dados_one_hot = dados_one_hot.values
# k_means_clustering(dados_one_hot, 4, 'tsne')

# st.text('''
#     Mas pesquisando um pouco mais afundo, descobrimos que o ideal para dados que possuem muitos valores categorigos, como no nosso
#     onde todos são categoricos, com exceção da idade, o ideal seria utilizar o K-modes, que é uma variação do K-mean, porém como o
#     nome diz, ao enves de utilizar média, utiliza moda.
# ''')


st.subheader('K-modes')


# max_clusters = st.slider("Escolha o Número Máximo de Clusters para o Método do Cotovelo", min_value=1, max_value=10, value=10)
# distortions = elbow_method_modes(dados, max_clusters)
# x_values=list(range(1,max_clusters +1))
# fig = go.Figure(dados=go.Scatter(x=x_values, y=distortions, mode='lines+markers'))

# fig.update_layout(
#     title="Método do Cotovelo",
#     xaxis_title="Número de Clusters",
#     yaxis_title="Distortion",
#     xaxis=dict(tickvals= x_values),
#     showlegend=False
# )

# st.subheader("Gráfico do Método do Cotovelo")
# st.plotly_chart(fig)

# st.text('''
#     Então fizemos uma função que gera os clusters utilizando o k-modes. Então geramso um gráfico de barra que mostra a distribuição 
#     de cada cluster. Não fizemos um gráfico de distribuição, que normalmente é o melhor tipo de visualização para clusters
#     porque, no k-modes os dados são mantidos como categorigos e não transformados em dados binarios utilizando o one hot encoding.
# ''')
#st.title('Aplicativo de Clustering com K-Modes e Gráfico da Silhueta')

# Carregamento dos dados (substitua 'seu_dataset.csv' pelo nome do seu arquivo de dados)
# data = pd.read_csv('data\data_cluster.csv')

# # Codificação dos dados categóricos com LabelEncoder
# encoder = LabelEncoder()
# for column in data.columns:
#     data[column] = encoder.fit_transform(data[column])

# # Sidebar para escolher o número de clusters
# n_clusters = st.sidebar.slider('Número de Clusters', min_value=2, max_value=10, value=4)

# # Calcular clusters
# km = KModes(n_clusters=n_clusters, init='Huang', n_init=10, verbose=0)
# clusters = km.fit_predict(data)

# # Calcular o coeficiente de silhueta
# silhouette_avg = silhouette_score(data, clusters, metric='hamming')
# silhouette_values = silhouette_samples(data, clusters, metric='hamming')

# st.write(f'Clusters: {clusters.tolist()}')
# # Exibir o coeficiente de silhueta
# st.write(f'Coeficiente de Silhueta: {silhouette_avg:.2f}')

# # Plotar o gráfico da silhueta com Plotly
# plot_silhouette(silhouette_avg, silhouette_values, clusters)

# # Defina cores personalizadas para cada cluster (RGB)
dados = pd.read_csv('data/fatal_encounters_tratado.csv')
clusters = k_modes_clustering(dados, 7)
dados['Cluster'] = clusters
distribuicao_Cluster(dados)







