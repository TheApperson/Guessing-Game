from flask import render_template, redirect, url_for, session, request
from flask_app import app
from flask import flash
import random
from flask_app.models.game import Game

@app.route('/')
def index():
    return redirect('/guesser')

@app.route('/guesser', methods=['GET', 'POST'])
def guesser():
    last_guess = 0
    last_answer = 0
    remaining_guess = 0
    win = False
    if 'answer' not in session:
        session['answer'] = random.randint(1, 1000)
        session['guess_min'] = 1
        session['guess_max'] = 1000
        session['turns_left'] = 10

    if request.method == 'POST':
        guess = request.form['guess']
        if int(session['turns_left']) == 1 and int(guess) != int(session['answer']):
            last_answer=session['answer']
            session['turns_left'] -= 1
            session.pop('answer', None)
        elif guess == "":
            flash("Enter a guess!","guess")
        elif int(guess) < int(session['guess_min']) or int(guess) > int(session['guess_max']):
            flash("Invalid guess","guess")
        elif int(guess) > session['answer']:
            last_guess = guess
            session['turns_left'] -= 1
            session['guess_max'] = guess
        elif int(guess) < session['answer']:
            last_guess = guess
            session['turns_left'] -= 1
            session['guess_min'] = guess
        else:
            last_guess = guess
            win = True
            last_answer=session['answer']
            session['turns_left'] -= 1
            remaining_guess = session['turns_left']
            session.pop('answer', None)
    return render_template('guesser.html', answer=session.get('answer'), guess_min=session.get('guess_min'),
    guess_max=session.get('guess_max'), last_guess = last_guess, win=win, turns_left=session.get('turns_left'), last_answer=last_answer, remaining_guess=remaining_guess)