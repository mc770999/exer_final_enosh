import os
from dotenv import load_dotenv
from proj_data.kafka_consume.kafka_consumer import consume_topic
from proj_data.mongo_consumer.service.models_service import insert_from_kafka_to_mongo

load_dotenv(verbose=True)

if __name__ == '__main__':
    try:
        topic_name = os.environ['MONGO_TOPIC']
        consume_topic(topic_name, insert_from_kafka_to_mongo)
    except Exception as e:
        print(e)
        pass
