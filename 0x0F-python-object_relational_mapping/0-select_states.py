#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.

Args:
    mysql_username: Username for the MySQL database.
    mysql_password: Password for the MySQL database.
    database_name: Name of the database to connect to.
"""

import MySQLdb


def main():
    """
    Connects to the MySQL database, retrieves all states sorted by id,
    and prints them.
    """
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")

    try:
        db = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database_name
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        for state in cursor.fetchall():
            print(state)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()