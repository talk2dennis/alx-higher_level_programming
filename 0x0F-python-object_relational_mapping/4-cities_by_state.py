#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N) from the
    database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password
    and database name
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c JOIN states AS s\
                 WHERE c.state_id = s.id\
                 ORDER BY c.id ASC")
    rows = cur.fetchall()
    for state in rows:
        print(state)
    cur.close()
    conn.close()
