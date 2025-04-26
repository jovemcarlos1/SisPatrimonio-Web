import streamlit as st
import controllers.MainController as MainController
import models.Game as game
import pandas as pd

def select():

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