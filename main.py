import streamlit as st
import controllers.MainController as MainController
import models.Game as game
import pandas as pd
import templates.pages.insert as Pageinsert
import templates.pages.select as Pageselect


st.set_page_config(
    page_title="SisPatrimonio",
    page_icon="favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

def get_version():
    with open("version.txt", "r") as f:
        return f.read().strip()

title, version = st.columns([5,1])

with title:
        st.title(':wrench: SisPatrimônio Web')

with version:
        st.markdown(f"###### Version`{get_version()}`")        

st.sidebar.title('Menu')
MainPage = st.sidebar.selectbox('Selecionar função:', ['Adicionar', 'Consultar', 'Alterar', 'Deletar'])

if MainPage == 'Adicionar':
        Pageinsert.insert()

if MainPage == 'Consultar':
        Pageselect.select()