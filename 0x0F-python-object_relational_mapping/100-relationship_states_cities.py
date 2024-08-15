from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine


def main():
    """
    Connects to the MySQL database, creates a new State with a City, and adds them to the database.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database_name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}', pool_pre_ping=True
    )

    # Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="California")

    # Create a new City object associated with the State
    new_city = City(name="San Francisco", state=new_state)

    # Add the State (which includes the City) to the session
    session.add(new_state)

    # Commit changes to the database
    session.commit()

    # Print confirmation message
    print("State and City added successfully")


if __name__ == "__main__":
    main()