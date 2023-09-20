import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import plotly.express as px
from scipy.cluster import hierarchy

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

def dendogram(data):
    linkage_matrix = hierarchy.linkage(data, method='ward')
    dendrogram = hierarchy.dendrogram(linkage_matrix, no_plot=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    hierarchy.dendrogram(linkage_matrix, ax=ax)
    st.subheader("Dendrograma")
    st.pyplot(fig)

def hierarchy_clustering(data, clusters_number):
    hc = AgglomerativeClustering(n_clusters=clusters_number, affinity='euclidean', linkage = 'ward')
    rotulos = hc.fit_predict(data)
    return rotulos

def custer_save(data, rotulos):
    data['Cluster'] = rotulos
    st.write(data)
    data.to_csv('data/data_cluster_hierarchical_4.csv', index=False)

def distribuição_por_cluster(columns, clustered_data):
    for col in columns:
        st.subheader(f"Distribuição de {col} por Cluster")
        fig_cat = px.histogram(clustered_data, x=col, color="Cluster", facet_col="Cluster")
        st.plotly_chart(fig_cat)

st.title('Final Antonio Neto')

dados_one_hot = pd.read_csv('data/fatal_encounters_one_hot_encoding.csv')

dendogram(dados_one_hot)
rotulos = hierarchy_clustering(dados_one_hot, 3)
st.subheader('Gráfico de dispersão utilizando PCA')
dimension_reducer_pca(dados_one_hot, rotulos, 3)
st.subheader('Gráfico de dispersão utilizando TSNE')
dimension_reducer_tsne(dados_one_hot, rotulos, 3)

# data = pd.read_csv('data/fatal_encounters_tratado.csv')
# custer_save(data, rotulos)

clustered_data = pd.read_csv('data/data_cluster_hierarchical.csv')
categorical_columns = ['Age', 'Cause_of_death', 'Subjects_gender', 'Region', 'Subjects_race']
distribuição_por_cluster(categorical_columns, clustered_data)  
