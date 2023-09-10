import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from prince import MCA


clustered_data = pd.read_csv("data/data_cluster.csv")
PK_clustered_data = pd.read_csv("data/PK_cluster.csv")

st.title("Análise dos Clusters")


def distribuição_por_cluster(columns, clustered_data):
    for col in columns:
        st.subheader(f"Distribuição de {col} por Cluster")
        fig_cat = px.histogram(clustered_data, x=col, color="Cluster", facet_col="Cluster")
        st.plotly_chart(fig_cat)


def plot_mca(data, clusters):
    mca = MCA(n_components=2)
    mca.fit(data)
    mca_result = mca.transform(data)
    
    fig = px.scatter(
        x=mca_result.iloc[:, 0],
        y=mca_result.iloc[:, 1],
        color=clusters,
        title="Visualização Multivariada (MCA) dos Clusters"
    )
    st.plotly_chart(fig)


def cluster_similarity(data, clusters):
    contingency_table = pd.crosstab(data['Cluster'], clusters)
    
    fig = px.imshow(
        contingency_table,
        labels=dict(x="Cluster Atual", y="Cluster Previsto", color="Contagem"),
        title="Matriz de Contingência - Similaridade entre Clusters"
    )
    st.plotly_chart(fig)


categorical_columns = ['Age', 'Cause_of_death', 'Subjects_gender', 'Region', 'Subjects_race']
distribuição_por_cluster(categorical_columns, clustered_data)    
st.subheader("Visualização Multivariada (MCA)")
plot_mca(clustered_data.drop('Cluster', axis =1), clustered_data['Cluster'])    


st.subheader("Similaridade entre Clusters")
cluster_similarity(clustered_data, clustered_data['Cluster'])


categorical_columns_2 = ["Symptoms of mental illness", "Unarmed/Did Not Have an Actual Weapon", "Alleged Weapon", "Fleeing", "Body Camera","Victims gender","Victims race"]
distribuição_por_cluster(categorical_columns_2, PK_clustered_data)
