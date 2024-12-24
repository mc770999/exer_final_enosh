from proj_data.postgres_consumer.database import session_maker, sead
from proj_data.postgres_consumer import Student, StudentReview, StudentLifeStyle, StudentCoursePerformance


def insert_models_to_db(model,json_list):

    with session_maker() as session:
        session.bulk_insert_mappings(model, json_list)
        session.commit()



with session_maker() as session:
    for s in list(session.query(StudentCoursePerformance).all()):
        print(s.student_id)

