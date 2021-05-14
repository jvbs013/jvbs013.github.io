import streamlit as st
import pandas as pd

st.sidebar.title("Paginas")
pagSelecionada=st.sidebar.selectbox("Selecione a pagina", ["Pagina principal", "Upload de arquivos"])

if pagSelecionada =="Pagina principal":
    titulo=st.title("Seja bem vindo")
    
if pagSelecionada== "Upload de arquivos":
    st.title("Upload arquivos")
    st.selectbox("Escolha o tipo do dado", ["Vendas", "Nome"])
    uploaded_file = st.file_uploader("Escolha sua planilha")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)