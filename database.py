import psycopg2
from elasticsearch import Elasticsearch

conn = psycopg2.connect("dbname=rag_db user=user password=password host=postgres")
cursor = conn.cursor()
cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS blog_embeddings (
        id SERIAL PRIMARY KEY,
        text TEXT,
        embedding VECTOR(1024)
    );
""")
conn.commit()

es = Elasticsearch(["http://elasticsearch:9200"])
if not es.indices.exists(index="blogs"):
    es.indices.create(index="blogs", body={"mappings": {"properties": {"text": {"type": "text"}, "embedding": {"type": "dense_vector", "dims": 1024}}}})
