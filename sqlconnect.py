import mysql.connector
from subtractionGame import *

cnx = mysql.connector.connect(user='root', password='Tikumamni123', host='localhost', database='connect')
cur = cnx.cursor()

# cur.execute("create table fibgame(size int(7), period int(7), start int(7));")
# cur.execute("desc fibgame;")

"""
for i in range(150):
    f = genFib(i)
    f.pop(0)
    period, start = solve(subtractionGame(f,50000))[0], solve(subtractionGame(f,50000))[1]
    op = "insert into fibgame(size, period, start) values(%s, %s, %s);"
    vals = (i,period,start)
    cur.execute(op, vals)
"""

cur.execute("select * from fibgame;")

f = open('fibData.txt','a')

for i in cur.fetchall():
    f.write(str(i) + '\n')
f.close()

cnx.commit()