from model_state import Base, State
from sqlalchemy import create_engine, delete


def main():
    """
    Connects to the MySQL database, deletes all states containing "a" in their name, and confirms the deletion count.
    """
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 4:
        print("Usage: ./model_state_delete_a.py <username> <password> <database_name>")
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

    # Build a delete query for states containing "a"
    deleted_count = session.query(State).filter(State.name.like("%a%")).delete(synchronize_session="fetch")

    # Commit the changes
    session.commit()

    print(f"{deleted_count} deleted")


if __name__ == "__main__":
    main()