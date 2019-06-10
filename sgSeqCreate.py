from subtractionGame import *
import mysql.connector

cnx = mysql.connector.connect(user='root', password='Tikumamni123', host='localhost', database='connect')
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



"""
p = "3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 3 5 5 3 5 3 5 3 5 5 3 5 3 5 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 3 5 3 5 5 5 3 5 3 5 5 3 5 5 3 5 3 5 5 5 3 5 3 5"
l = list(map(int, p.split(' ')))
t,f = 0,0
for i in l:
    if i == 3:
        t += 1
    else:
        f += 1
print(t,f)"""

"""
f = open('fibData11.txt','r')
l = f.readlines()
print(l)
tuples = []
for i in l:
    x = i[1:-2]
    l = x.split(', ')
    tuples.append(tuple(map(int, l)))

for i in tuples:
    cur.execute("update fibgame set start = %d where size = %d;" % (i[2],i[0]))

cnx.commit()"""
