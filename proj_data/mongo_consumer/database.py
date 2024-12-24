import os

from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv(verbose=True)


DATABASE_MONGO_URL="mongodb://admin:1234@172.30.156.27:27017/"
# MongoDB connection details
print(os.environ["DATABASE_MONGO_URL"])
client = MongoClient(DATABASE_MONGO_URL)

# Access a database (creates it if it doesn't exist)
db = client["students_and_teachers"]

# Access a collection (creates it if it doesn't exist)
students_db = db["students"]
course_db = db["course"]
teacher_db = db["teacher"]


