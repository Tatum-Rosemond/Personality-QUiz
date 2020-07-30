# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import School

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods= ['GET', 'POST'])
def results():
    Subject = request.form["Subject"]
    Character=School(Subject)
    return render_template("results.html",Character=Character)
