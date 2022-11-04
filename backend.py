import sqlite3
import random


def db_call(sql, sql_values):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(sql, sql_values)
    result = cur.fetchall()
    return result


    
def db_call_all(sql):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return result 


def randomColor():
    rc = random.choices(range(255), k=3)
    return rc


class Poem:
    sql = "SELECT eng, rowid FROM new_table ORDER BY random() LIMIT (?)"
    sql_values = (4,)

    def __init__(self, **kwargs) -> None:
        self.color = randomColor()
        if kwargs:
            self.__dict__.update(kwargs)
            discreteSQL = "SELECT id, eng FROM new_table WHERE id IN (?,?,?,?)"
            poem_object = db_call(discreteSQL, self.lineNums)
            poem_dict = {x:y for x,y in poem_object}
           
            self.lines = [poem_dict.get(int(x)) for x in self.lineNums]
           
            ucode = self.code.replace("-","_")
            # js objects can't start with a number - not sure this is needed anymore though
            self.ucode = "U" + ucode
        else:
            self.lines = []
            self.lineNums = []
            self.code = ""
            poemPrim = db_call(self.sql, self.sql_values)
            for i in poemPrim:
                self.lines.append(i[0])
                self.lineNums.append(i[1])
            self.code = "-".join(str(x) for x in self.lineNums)
            ucode = self.code.replace("-","_")
            self.ucode = "U" + ucode

    def __repr__(self) -> str:
        return f"Code = {self.code}\n Lines = {[str(line) for line in self.lines]}\n"

    def bbcode(self):
        return f"[quote={self.code}]{self.lines[0]}\n {self.lines[1]}\n {self.lines[2]}\n {self.lines[3]}\n[/quote]"

def getMultiplePoems(num=10):
    multiplePoems = []
    for _ in range(num):
        multiplePoems.append(Poem())
    return multiplePoems

def listAllPoems():
    all_lines = db_call_all("SELECT eng_phrase, cn_phrase from phrase")
    return all_lines



