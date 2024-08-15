from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base


class City(Base):
    """
    City class representing a city in a state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State')  # Relationship with the State class

    def __repr__(self):
        """
        String representation of a City object.
        """
        return f"<city id={self.id}> {self.name}"