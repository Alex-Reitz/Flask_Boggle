from boggle import Boggle
from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

from boggle import game_board

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    board = game_board.make_board()
    session["board"] = board
    return render_template("home.html", board=board)
