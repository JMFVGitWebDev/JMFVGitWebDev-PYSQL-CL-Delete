import os
import sqlite3

"""
SQL sublanguage: DML (Data Manipulation Language)

The "DELETE" keyword is utilized to remove records based on a condition.

The syntax for deleting records from a table is as follows:
DELETE FROM table_name WHERE condition;

NOTE: Whenever you execute a DELETE statement, have a WHERE condition that identifies exactly what records you
would like to delete. Leaving this out will remove ALL records from the table.
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    Assignment: In the problem1.sql, write the SQL command to delete 'Steve' from the site_user table, assuming
    that the table and 'Steve' records already exist.

           site_user table:
           |   id  |     firstname        |
           --------------------------------
           |1      |'Steve'               |
           |2      |'Alexa'               |
           |3      |'Steve'               |
           |4      |'Brandon'             |
           |5      |'Adam'                |

    Sets up the site_user table, runs the student's statement against it, and returns the open connection so
    the caller can verify who remains.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE site_user (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname varchar(100));")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Steve');")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Alexa');")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Steve');")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Brandon');")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Adam');")
    conn.commit()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
