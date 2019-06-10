from subtractionGame import *
import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='localhost', database='connect')
cur = cnx.cursor()

cur.execute("select * from fibgame;")
f = open('periodBlocks.txt','a')


for i in cur.fetchall()[3:]:
    n, p, n0 = i
    fib = genFib(n)
    sg = subtractionGame(fib, 500000)
    periodBlock = encode(sg[n0 : n0 + p])
    f.write(periodBlock + "\n")
f.close()
