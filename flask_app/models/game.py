import random
from flask_app.controllers import users

class Game:
    db_name = "game_hub_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.play_count = data['play_count']
        self.high_score = data['high_score']
        self.win = data['win']
        self.loss = data['loss']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO game (name, play_count, high_score, win, loss) VALUES (%(name)s, %(play_count)s, %(high_score)s, %(win)s, %(loss)s);"
        user_id = connectToMySQL(cls.db_name).query_db(query, data)
        return user_id
