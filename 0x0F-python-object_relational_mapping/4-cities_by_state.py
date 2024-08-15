#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa with state names.

Args:
    mysql_username: Username for the MySQL database.
    mysql_password: Password for the MySQL database.
    database_name: Name of the database to connect to.
"""

import MySQLdb


def main():
    """
    Connects to the MySQL database, retrieves all cities with state names,
    and prints them in a single query using JOIN.
    """
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")

    try:
        db = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database_name
        )
        cursor = db.cursor()
        query = """
            SELECT cities.id, cities.name, states.name AS state
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
        cursor.execute(query)
        for city, state in cursor.fetchall():
            print(f"{city[0]:d}, {city[1]:s}, {state}")

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()