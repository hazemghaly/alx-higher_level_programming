#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''


import sys
import MySQLdb
''' Module For Connecting To MySQL database'''

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = '''
    SELECT COALESCE(cities.name, 'No cities'
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    WHERE states.name Like %s
    '''
    cursor.execute(query, (sys.argv[4] + '%',))
    cities = cursor.fetchall()
    ci = [city[1] for city in cities if city[4] == sys.argv[4]]
    if not ci:
        print("")
    else:
        print(", ".join(ci))
    cursor.close()
    db.close()
