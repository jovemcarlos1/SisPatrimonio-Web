import services.database as db;
import models.Game as game;
import pandas as pd; 

def INSERT(game):
    db.cursor.execute("""
    INSERT INTO Steam(GameName, GameCategory, GamePrice, GameReleaseDate)
    VALUES(?,?,?,?)""",
    game.gamename, game.category, game.price, game.releasedate)
    db.conn.commit()
    db.conn.close()
    
    
    
# def SELECT(game):
#     db.cursor.execute("""
#     SELECT * FROM DB_Steam WHERE GameID = ?""", game.id)

#     resultados = db.cursor.fetchall()

#     colunas = [desc[0] for desc in db.cursor.descripton]
#     df = pd.DataFrame(resultados, columns=colunas)
#     db.cursor.close()
#     db.conn.close()
#     return df

def SELECT_BY_ID(gameid):
    db.cursor.execute("SELECT * FROM STEAM WHERE GameID = ? ", (gameid,)).rowcount(4)
    list = []
    
    for row in db.cursor.fetchall():
        list.append()  
    
    
    
