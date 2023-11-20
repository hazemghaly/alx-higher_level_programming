#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''


import sys
import MySQLdb
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM cities INNER JOIN states ON cities.state_id = states.id')
    cities = cursor.fetchall()
    for city in (cities):
        print(city)
    cursor.close()
    db.close()
