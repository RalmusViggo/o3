from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/brukere.html')
def vis_brukere():
    return render_template("brukere.html", brukere = ["alice", "bob", "carol", "david", "eve"])


if __name__ == "__main__":
    app.run() 