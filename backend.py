import sqlite3
import random


def db_call(sql, sql_values):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = cur.execute(sql, sql_values)
    result = cur.fetchall()
    return result


def randomColor():
    rc = random.choices(range(255), k=3)
    return rc


class Poem:
    sql = "SELECT eng_phrase, rowid FROM phrase ORDER BY random() LIMIT (?)"
    sql_values = (4,)

    def __init__(self) -> None:
        self.lines = []
        self.lineNums = []
        self.code = ""
        self.color = randomColor()
        poemPrim = db_call(self.sql, self.sql_values)
        for i in poemPrim:
            self.lines.append(i[0])
            self.lineNums.append(i[1])
        self.code = "-".join(str(x) for x in self.lineNums)

    def __repr__(self) -> str:
        return f"Code = {self.code}\n Lines = {[str(line) for line in self.lines]}\n"


def getMultiplePoems(num=10):
    multiplePoems = []
    for _ in range(num):
        multiplePoems.append(Poem())
    return multiplePoems
