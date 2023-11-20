#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''


import sys
import MySQLdb
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    N_and_n_que = "SELECT * FROM states WHERE name LIKE %s"
    cursor.execute(N_and_n_que, ('N%',))
    states_N = cursor.fetchall()
    cursor.execute(N_and_n_que, ('n%',))
    states_n = cursor.fetchall()
    states = states_N + states_n
    for state in states:
        print(state)
    cursor.close()
    db.close()
