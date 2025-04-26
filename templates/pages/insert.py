import streamlit as st
import controllers.MainController as MainController
import models.Game as game
import pandas as pd

def insert():
    
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