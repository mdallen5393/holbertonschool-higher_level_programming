#!/usr/bin/python3
"""
This script lists all `states` from the database
`hbtn_0e_0_usa` starting with `N`.
"""
import MySQLdb
import sys


def filter_states():
    """
    lists all states
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
ORDER BY id;".format(sys.argv[4]))

    results = cur.fetchall()

    cur.close()
    db.close()

    for row in results:
        print(row)


if __name__ == "__main__":
    filter_states()
