from flask import Flask, render_template
from backend import getMultiplePoems, Poem, listAllPoems


app = Flask(__name__)


@app.route("/")
def indexPoem():
    return render_template('index.html')


@app.route('/mc')
def poemsList():
    poems = getMultiplePoems()
    return render_template('poems_list.html', poems=poems)

@app.route('/poem/<code>')
def onePoem(code):
    id_list = code.split('-')
    poem = Poem(lineNums=id_list, code=code)

    return render_template('one_poem.html', poem=poem, id_list=id_list)

@app.route('/list')
def all_lines():
    all_lines = listAllPoems()
    return render_template('allPoems.html', all_lines=all_lines)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
