from proj_data.neo4j_consumer.database import driver


def create_nodes(student_id, teacher_id, class_id):
    with driver.session() as session:
        query = """
                    merge (n1:Student{student_id:$student_id})
                    merge (n2:Teacher{teacher_id:$teacher_id})
                    merge (n3:Class{class_id:$class_id}) 
                    merge (n1)  -[:ENROLLED_IN]-> (n3)
                    merge (n2)  -[:TEACH_IN]-> (n3)
                    return *
                """
        params = {
            'student_id' : student_id,
            "teacher_id" : teacher_id,
            "class_id" : class_id
        }
        res = session.run(query, params).data()
        return  next((r for r in res),{}).get("n", {})