from flask import Flask, json, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from backend import *

app = Flask(__name__)

def getPoem(lines = 4):
    poem = Poem()
    return poem

@app.route("/")
def indexPoem():
    return render_template('index.html')

@app.route("/api")
def apiPoem():
    poem = getPoem()
    return jsonify(poem)

@app.route("/htmx")
def htmxRoute():
    poem = getPoem()
    return render_template('poem.html', poem=poem)





if __name__ == "__main__":
    app.run(host='0.0.0.0')
