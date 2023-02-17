import random
from flask_app.controllers import users

games = 0

def add_game():
    global games
    games += 1
    return games

"""class Game:
    def __init__(self, answer, guess_min, guess_max, turns_left, last_guess, last_answer, remaining_guess):
        self.answer = random.randint(1,1000)
        self.guess_min = 1
        self.guess_max = 1000
        self.turns_left = 15
        self.last_guess = 0
        self.last_answer = 0
        self.remaining_guess = 0"""