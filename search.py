import numpy as np
from database import conn, cursor, es

def search_exact_match(query):
    cursor.execute("SELECT * FROM blog_embeddings WHERE text ILIKE %s LIMIT 5;", ("%" + query + "%",))
    return cursor.fetchall()

def search_semantic(query_vector):
    cursor.execute("SELECT id, text, embedding <=> %s AS distance FROM blog_embeddings ORDER BY distance LIMIT 5;", (query_vector,))
    return cursor.fetchall()

def search_elasticsearch(query_vector):
    response = es.search(index="blogs", body={"query": {"script_score": {"query": {"match_all": {}}, "script": {"source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0", "params": {"query_vector": query_vector}}}}})
    return response['hits']['hits']
