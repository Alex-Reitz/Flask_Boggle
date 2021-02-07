from boggle import Boggle
from flask import Flask, render_template, session, jsonify, request, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()
Guesses = []
board = boggle_game.make_board()

@app.route("/")
def home_page():
    session["board"] = board
    session["guess_tracker"] = Guesses
    return render_template("home.html", board=board)

@app.route("/", methods=[ 'POST'])
def guess_to_server():
        answer = request.form["guess"]
        print(answer)
        #Save guess in session list
        Guesses = session["guess_tracker"]
        Guesses.append(answer)
        session["guess_tracker"] = Guesses
        #Check if word is valid
        validatedAnswer = boggle_game.check_valid_word(board, answer)
        return jsonify(validatedAnswer)

    