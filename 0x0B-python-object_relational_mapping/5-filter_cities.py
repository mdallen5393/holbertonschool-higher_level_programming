#!/usr/bin/python3
"""
This script lists all `states` from the database
`hbtn_0e_0_usa` starting with `N`.
"""
import MySQLdb
import sys


def cities_by_states():
    """
    lists all states
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT name \
                   FROM cities \
                  WHERE state_id = (SELECT id \
                                      FROM states \
                                    WHERE name=%(target)s) \
                  ORDER BY id;",
                {'target': sys.argv[4]})

    results = cur.fetchall()

    cur.close()
    db.close()

    if len(results) <= 0:
        print()
        return

    for i in range(len(results) - 1):
        print(results[i][0], end=', ')
    print(results[len(results) - 1][0])


if __name__ == "__main__":
    cities_by_states()
