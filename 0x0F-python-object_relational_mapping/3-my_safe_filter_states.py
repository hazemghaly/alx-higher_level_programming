#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''


import sys
import MySQLdb
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    sql_que = "SELECT * FROM states WHERE name like %s".format(sys.argv[4])
    cursor.execute(sql_que, (sys.argv[4] + '%',))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
