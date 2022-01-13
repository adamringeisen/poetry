import sqlite3
from flask_sqlalchemy import SQLAlchemy


""" def getDict(data):
    D =dict(lines, [(1, data[0][0]), (2, data[1][0]), (3,  data[2][0]), (4, data[3][0])]),
    (code, f"{data[0][1]}-{data[1][1]}+{data[2][1]}+{data[3][1]}")

    ) 
    return D
"""
D = {"lines" : [], "code" : []}

def getPoem(lines = 4, ):
    con = sqlite3.connect('database.db')
    # con.row_factory = sqlite3.Row
    cur = con.cursor()
    poemQuery = cur.execute("SELECT eng_phrase, rowid FROM phrase ORDER BY random() LIMIT (?)", (lines,))
    poemPrim = cur.fetchall()
    for i in poemPrim:
        D["lines"].append(i[0])
        D["code"].append(i[1])
    # print(D["lines"])
    return D



# getPoem()
# mp = getMultiplePoems()
# print(D)

#mulp = [('I am told that you dance wonderfully well.', 746), ('The sudden barking frightened Clara.', 617), ('Are your grandparents still living?', 568), ('He knows English better than I.', 456), ('Slow down!', 38), ('Your English is improving little by little.', 788), ('I regret to inform you that we are unable to offer you employment.', 971), ('He sat with his arms across the chest.', 657), ('The bat together with the balls was stolen.', 774), ('His cake is four times as big as mine.', 659), ('He is physically mature.', 269), ('Forget it!', 33), ('I think you have the wrong number.', 551), ('He invited me to dinner yesterday.', 543), ('What shall we do tonight?', 294), ('Please push the ladder against the wall.', 730), ('There are many stars in the sky.', 500), ('Oh, you are kidding me.', 237), ('No pain, no gain.', 119), ("There isn't any water in the bottle.", 620), ('Love me, love my dog.', 191), ('Even a child can answer this question', 654), ('They are only too delighted to accept the invitation.', 922), ('I wish I knew my neighbor.', 318), ('This one cannot compare with that one.', 673), ('We get to London this afternoon.', 501), ('The harder I study, the better my English will be.', 871), ('May I know the quantity you require?', 612), ('It is growing cool.', 157), ('My father is at home looking for the ticket.', 801), ('15 divided by 3 equals 5.', 265), ('I will be back by the end of next month.', 726), ("I'm in a hurry!", 90), ('There go the house lights.', 328), ('Show your tickets, please.', 324), ("These shoes don't fit right.", 391), ('I develop films myself.', 251), ('I walked across the park.', 276), ('Could you tell me where I can wash my hands?', 789), ('The sight of the dead body scared him stiff.', 805)]
#print(len(mulp))

def db_call(sql, sql_values):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    query = cur.execute(sql, sql_values)
    result = cur.fetchall()
    return result


class Poem:
    sql = "SELECT eng_phrase, rowid FROM phrase ORDER BY random() LIMIT (?)"
    sql_values = (4,)
    
    def __init__(self) -> None:
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

np = getMultiplePoems()


print(np)