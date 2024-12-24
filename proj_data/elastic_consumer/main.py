import os
from dotenv import load_dotenv

from proj_data.elastic_consumer.service.elastic_service import insert_to_elastic_from_kafka
from proj_data.kafka_consume.kafka_consumer import consume_topic

load_dotenv(verbose=True)

if __name__ == '__main__':
    try:
        topic_name = os.environ['ELASTIC_SEARCH_TOPIC']
        consume_topic(topic_name, insert_to_elastic_from_kafka)
    except KeyboardInterrupt:
        pass
