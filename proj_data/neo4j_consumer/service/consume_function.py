from proj_data.neo4j_consumer.repository.neo4j_repository import create_nodes


def insert_from_kafka_to_neo4j(key, values):
    for value in values:
        student_id = value.get("student_id", "no_student")
        teacher_id = value.get("teacher_id", "no_teacher")
        class_id = value.get("class_id", "no_class")
        create_nodes(student_id, teacher_id, class_id)