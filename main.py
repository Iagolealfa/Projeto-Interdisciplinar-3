import streamlit as st
import dataAll



st.set_page_config(
    page_title = "Police Shooting",
    layout = "wide")

def barra_Lateral():
    app_selection = st.sidebar.radio("Páginas", ("All Dataset", "Analise Graficos"))

    if app_selection == "All Dataset":
        dataAll.run()
    
        
       
    

def main():
    barra_Lateral()

if __name__ == "__main__":
    main()