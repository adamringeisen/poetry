from flask import Flask, json, render_template, jsonify
from backend import getMultiplePoems


app = Flask(__name__)


@app.route("/")
def indexPoem():
    return render_template('index.html')

@app.route('/mc')
def poemsList():
    poems = getMultiplePoems()
    return render_template('poems_list.html', poems=poems)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
