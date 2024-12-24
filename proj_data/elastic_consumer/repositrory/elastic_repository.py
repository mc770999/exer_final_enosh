from proj_data.elastic_consumer.elastic_database import es_client
from elasticsearch.helpers import bulk


def insert_meny(documents, index_name):
    actions = [
        {
            "_op_type": "index",  # Index operation
            "_index": index_name,  # Target index
            "_source": doc  # The document content
        }
        for doc in documents
    ]

    # Insert documents using the bulk helper
    try:
        success, failed = bulk(es_client, actions)
        print({"success": success, "failed": failed})# Pass the client directly
        return {"success": success, "failed": failed}
    except Exception as e:
        print(f"Bulk insert failed: {e}")
        print({"success": 0, "failed": len(documents)})
        return {"success": 0, "failed": len(documents)}

# Example usage
result = insert_meny([{"name": "maenchem"}, {"name": "menachem2"},], "test3")
print(result)