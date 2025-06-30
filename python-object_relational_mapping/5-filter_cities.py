#!/usr/bin/python3
"""Script that takes the name of states as an argument then displays
all cities of the state"""
import re

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2],db=argv[3])
    except Exception:
        print("Can't connect to database")
        exit(0)
    state = argv[4]
    if re.search('^[a-zA-Z]+$', state) is None:
        print('Please enter a valid name State')
        exit(1)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id=states.id\
                    WHERE states.name = '{:s}' ORDER BY cities.id ASC;".format(state))

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
