import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title = "Análise de Dados",
    layout = "wide",
    menu_items = {
        'About': "TESTE DO ABOUT"
    }
)

st.title('Análise de Dados')

data = pd.read_csv('../data/shootings_wash_post.csv')
st.write(data)
st.title('Quantidade de mortes com separação de raça por estado')
grouped_data = data.groupby(['state', 'race']).size().unstack(fill_value=0)


fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.plot(kind='bar', stacked=True, ax=ax)


ax.set_xlabel('Estado')
ax.set_ylabel('Quantidade')
ax.legend(title='Raça', title_fontsize='11', fontsize='9')


plt.tight_layout()


st.pyplot(fig)
