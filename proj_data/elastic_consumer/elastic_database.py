import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Load environment variables from .env file
load_dotenv(verbose=True)





# Create the Elasticsearch client
es_client = Elasticsearch(
    ["http://localhost:9200"],
    basic_auth=("elastic", "123456"),
    verify_certs=False
)


