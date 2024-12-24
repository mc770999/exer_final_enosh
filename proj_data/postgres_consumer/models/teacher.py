from sqlalchemy import Column, String
from proj_data.postgres_consumer import Base

class Teacher(Base):
    __tablename__ = 'professors'  # Name of the table

    id = Column(String, primary_key=True)  # Assuming 'id' is unique
    name = Column(String, nullable=False)  # Name of the professor
    department = Column(String, nullable=False)  # Department name
    title = Column(String, nullable=False)  # Title of the professor
    office = Column(String, nullable=False)  # Office location
    email = Column(String, nullable=False)  # Email (unique)
