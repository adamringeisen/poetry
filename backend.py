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

    def __init__(self, **kwargs) -> None:
        self.color = randomColor()
        if kwargs:
            self.__dict__.update(kwargs)
            discreteSQL = "SELECT eng_phrase FROM phrase WHERE rowid=(?) OR rowid=(?) OR rowid=(?) OR rowid=(?)"
            lines = db_call(discreteSQL, self.lineNums)
            # The db doesn't return the lines in order so we have to put them back
            linesOrder = [sorted(self.lineNums).index(i) for i in self.lineNums]
            lines = [lines[i] for i in linesOrder]
            self.lineList = lines
            self.lines = [line[0] for line in lines]
        else:
            self.lines = []
            self.lineNums = []
            self.code = ""
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


