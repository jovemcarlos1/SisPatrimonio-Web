import services.database as db;
import models.Game as game;
import pandas as pd; 

def INSERT(game):
    db.cursor.execute("""
    INSERT INTO DB_Steam(GameName, GameCategory, GamePrice, ReleaseDate)
    VALUES(?,?,?,?)""",
    game.name, game.category, game.price, game.releasedate).rowcount
    db.conn.commit()
    db.cursor.close()
    
    
# def SELECT(game):
#     db.cursor.execute("""
#     SELECT * FROM DB_Steam WHERE GameID = ?""", game.id)

#     resultados = db.cursor.fetchall()

#     colunas = [desc[0] for desc in db.cursor.descripton]
#     df = pd.DataFrame(resultados, columns=colunas)
#     db.cursor.close()
#     db.conn.close()
#     return df

def SELECT_BY_ID(game_id):
    db.cursor.execute("SELECT * FROM DB_STEAM WHERE GameID = ?", (game_id))
    row = db.cursor.fetchone()  # Pega apenas um resultado

    if row:
        return game.Game(row[0], row[1], row[2], row[3], row[4])  # Retorna o objeto Game
    else:
        return None  # Retorna None se não encontrar o jogo
