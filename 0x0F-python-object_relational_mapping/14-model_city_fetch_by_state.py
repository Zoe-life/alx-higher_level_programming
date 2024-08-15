from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select


def main():
    """
    Connects to the MySQL database, retrieves all City objects from a state, and prints them.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./model_city_fetch_by_state.py <username> <password> <database_name>")
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

    # Query for all City objects sorted by id
    query = select(City).join(State).order_by(City.id)

    # Iterate over City objects and print them with their state name
    for city in query.all():
        print(f"{city.state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    main()