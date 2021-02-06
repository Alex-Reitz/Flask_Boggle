from boggle import Boggle
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    return render_template("home.html")
