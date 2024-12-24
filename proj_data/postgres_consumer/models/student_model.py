from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from proj_data.postgres_consumer import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=True)

    # Establishing relationships with StudentLifeStyle and StudentReview
    life_style = relationship("StudentLifeStyle", back_populates="student", cascade="all, delete-orphan")
    reviews = relationship("StudentReview", back_populates="student", cascade="all, delete-orphan")
    study_data = relationship("StudentCoursePerformance", back_populates="student", cascade="all, delete-orphan")