from fastapi import FastAPI
from search import search_exact_match, search_semantic, search_elasticsearch
from embedder import get_embedding

app = FastAPI()

@app.get("/search")
def search(query: str):
    query_vector = get_embedding(query)
    exact_results = search_exact_match(query)
    semantic_results = search_semantic(query_vector)
    elastic_results = search_elasticsearch(query_vector)
    return {"exact": exact_results, "semantic": semantic_results, "elasticsearch": elastic_results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
