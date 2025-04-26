import streamlit as st
import controllers.MainController as MainController
import models.Game as game
import pandas as pd


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

        st.title('Adicionar')
        with st.form(key='include_game'):
                input_gamename = st.text_input(label='Jogo:')
                input_category = st.text_input(label='Categoria:')
                input_price = st.number_input(label='Preço:',step=0.50)
                input_releasedate = st.date_input(label='Ano de Lançamento:', format= "DD/MM/YYYY")
                input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
                
                MainController.INSERT(game.Game(0 , input_gamename, input_category, input_price, input_releasedate))
                st.success(f'Cadastro realizado!')    

if MainPage == 'Consultar':
        
        st.title('Consultar')
        with st.form(key='search_game'):
                input_gameid = st.text_input(label='ID:')
                input_button_submit = st.form_submit_button('Consultar')
        if input_button_submit:
                if input_gameid.isdigit():  # Garante que o ID é um número válido
                        game = MainController.SELECT_BY_ID(input_gameid)  # Chama a função corretamente

                if game:
                        st.success(f"Jogo encontrado: {game.row[1]}")
                        st.write(f"**Categoria:** {game.row[2]}")
                        st.write(f"**Preço:** R$ {game.row[3]}")
                        st.write(f"**Data de Lançamento:** {game.row[4]}")
                else:
                        st.error("Jogo não encontrado.")
                
