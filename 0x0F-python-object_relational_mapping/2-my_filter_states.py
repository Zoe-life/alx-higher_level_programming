#!/usr/bin/python3
"""
This script lists all values in the states table where the name matches the argument.

Args:
    mysql_username: Username for the MySQL database.
    mysql_password: Password for the MySQL database.
    database_name: Name of the database to connect to.
    state_name: Name of the state to search for.
"""

import MySQLdb


def main():
    """
    Connects to the MySQL database, retrieves states matching the argument sorted by id,
    and prints them.
    """
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")
    state_name = input("Enter state name to search: ")

    try:
        db = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database_name
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        for state in cursor.fetchall():
            print(state)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()