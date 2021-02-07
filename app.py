from boggle import Boggle
from flask import Flask, render_template, session, jsonify, request, redirect, make_response
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
CORS(app)
debug = DebugToolbarExtension(app)

boggle_game = Boggle()
Guesses = []
board = boggle_game.make_board()

@app.route("/", methods=["GET","POST"])
def home_page():
    if(request.method == "POST"):
        req = request.get_json()
        answer = request.form["guess"]
        #Save guess in session list
        Guesses = session["guess_tracker"]
        Guesses.append(answer)
        session["guess_tracker"] = Guesses
    #Check if word is valid
        validatedAnswer = boggle_game.check_valid_word(board, answer)
        return jsonify(validatedAnswer)
    else: 
        return render_template("home.html", board=board)

   

    