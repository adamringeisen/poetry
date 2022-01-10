import csv
import random
import sqlite3
from flask import Flask, json, render_template, jsonify

app = Flask(__name__)


def getPoem(lines = 4):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    poemQuery = cur.execute("SELECT eng_phrase, rowid FROM phrase ORDER BY random() LIMIT (?)", (lines,))
    poem = cur.fetchall()
    return poem



@app.route("/")
def indexPoem():
    # poem = getPoem()
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
