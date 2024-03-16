#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database
    name and state name (SQL injection free!)
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM cities AS c JOIN states AS s\
                 ON c.state_id = s.id\
                 WHERE s.name = %s\
                 ORDER BY c.id ASC", (argv[4],))
    rows = cur.fetchall()
    cities = ", ".join(row[0] for row in rows)
    print(cities)
    cur.close()
    conn.close()
