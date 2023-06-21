import sqlite3
import re
from constants import *

def database_game(name, score):
    list_scores = []
    with sqlite3.connect(DATABASE) as connection:
        if re.match(r"^[A-Za-z0-9]+$", name):
            sentence = "INSERT INTO player_scores(name, score) VALUES (?,?)"
            connection.execute(sentence, (name, score))
            connection.commit()
        else:
            print("Error Insert")
        try: 
            sentence = "SELECT * FROM player_scores ORDER BY score DESC LIMIT 10"
            cursor = connection.execute(sentence)
            list_scores = cursor.fetchall()
        except:
            print("Error Select")
    return list_scores