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
    

def SELECT_BY_ID(gameid):
    db.cursor.execute("SELECT * FROM STEAM WHERE GameID = ? ", (gameid,)).rowcount(4)
    list = []
    
    for row in db.cursor.fetchall():
        list.append()  
