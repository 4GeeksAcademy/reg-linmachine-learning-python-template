

# your code here
from flask import Flask, render_template
from utils import db_connect

engine = db_connect()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Puedes agregar más rutas si lo necesitas
