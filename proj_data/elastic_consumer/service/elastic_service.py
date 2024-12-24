from proj_data.elastic_consumer.repositrory.elastic_repository import insert_meny


def insert_to_elastic_from_kafka(key, value):
    try:
        print(key)
        insert_meny(value,key)
    except Exception as e:
        print(e)