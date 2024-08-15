#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.

Args:
    mysql_username: Username for the MySQL database.
    mysql_password: Password for the MySQL database.
    database_name: Name of the database to connect to.
    state_name: Name of the state to search for.
"""

import MySQLdb


def main():
    """
    Connects to the MySQL database, retrieves all cities of a state,
    and prints them in a single query using JOIN.
    """
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")
    state_name = input("Enter state name: ")

    try:
        db = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database_name
        )
        cursor = db.cursor()
        query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()

        if not cities:
            print(f"No city found in {state_name}")
            return

        print(", ".join(city[0] for city in cities))

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()