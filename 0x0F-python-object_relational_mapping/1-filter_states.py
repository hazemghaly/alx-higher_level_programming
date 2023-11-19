#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''


import sys
import MySQLdb
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    a = "N"
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states_starting_with_n = cursor.fetchall()
    for state in states_starting_with_n:
        print(state)
    cursor.close()
    db.close()
