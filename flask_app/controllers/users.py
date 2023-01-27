from flask import render_template, redirect, url_for, session, request
from flask_app import app
from flask import flash
import random


@app.route('/')
def index():
    return redirect('/guesser')

def build_list(x):
    result = []
    for i in range(x+1):
        if i == 0:
            pass
        else:
            result.append(i)
    return result

@app.route('/guesser', methods=['GET', 'POST'])
def guesser():
    build_list(1000)
    if request.method == 'POST':
        last_guess = 0
        last_answer = 0
        remaining_guess = 0
        guess = request.form['guess']
        if 'answer' not in session:
            session['answer'] = random.randint(1, 1000)
            session['guess_min'] = 1
            session['guess_max'] = 1000
            session['turns_left'] = 15
        else:
            if int(session['turns_left']) == 1:
                last_answer=session['answer']
                flash(f"No more guesses.. you lose! :( The answer was {last_answer}", "guess")
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
                remaining_guess = session['turns_left']
                flash(f"You win! With {remaining_guess -1} guesses left.", "guess")
                session.pop('answer', None)
        return render_template('guesser.html', answer=session.get('answer'), guess_min=session.get('guess_min'),
        guess_max=session.get('guess_max'), guess = last_guess, turns_left=session.get('turns_left'), last_answer=last_answer, remaining_guess=remaining_guess)
    return render_template('guesser.html')