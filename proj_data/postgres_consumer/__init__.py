
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
Base = declarative_base()

from .models.course_model import Course
from .models.student_model import Student
from .models.teacher import Teacher
from .models.student_review import StudentReview
from .models.student_life_style import StudentLifeStyle
from .models.student_course_performance import StudentCoursePerformance



