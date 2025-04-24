import streamlit as st
import controllers.MainController as MainController
import models.Game as game
import pandas as pd


st.set_page_config(
    page_title="projectCRUD",
    page_icon="favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)


st.sidebar.title('Menu')
MainPage = st.sidebar.selectbox('Selecionar função:', ['Adicionar', 'Consultar', 'Alterar', 'Deletar'])

if MainPage == 'Adicionar':

        st.title('Adicionar')
        with st.form(key='include_game'):
                input_gamename = st.text_input(label='Jogo:')
                input_category = st.text_input(label='Categoria:')
                input_price = st.number_input(label='Preço:',step=0.50)
                input_releasedate = st.date_input(label='Ano de Lançamento:')
                input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
                game.name = input_gamename
                game.category = input_category
                game.price = input_price
                game.releasedate = input_releasedate
                
                MainController.INSERT(game.Game(input_gamename, input_category, input_price, input_releasedate))
                st.success(f'Cadastro realizado!')    

if MainPage == 'Consultar':
        st.title('Consultar')
        with st.form(key='search_game'):
                input_gameid = st.text_input(label='ID:')
                input_button_submit = st.form_submit_button('Consultar')
        if input_button_submit:
                if input_gameid.isdigit():  # Garante que o ID é um número válido
                        game = MainController.SELECT_BY_ID(int(input_gameid))  # Chama a função corretamente

                if game:
                        st.success(f"Jogo encontrado: {game.name}")
                        st.write(f"**Categoria:** {game.category}")
                        st.write(f"**Preço:** R$ {game.price}")
                        st.write(f"**Data de Lançamento:** {game.releasedate}")
                else:
                        st.error("Jogo não encontrado.")
                
               

