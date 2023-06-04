from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Response
from collection import collection, client

from PostParams import PostParams
from DeleteParams import DeleteParams

app = FastAPI()

@app.get("/")
async def read_root(q: str, partner: str = None):
    where = None
    if partner:
        where = {"partner": partner}

    result = collection.query(
        query_texts=[q],
        n_results=100,
        where=where,
        include=[]
    )
    return result

@app.post("/")
async def read_root(params: PostParams):
    collection.upsert(
        ids=[params.id],
        metadatas=[{"partner": params.partner}],
        documents = [params.document],
    )
    client.persist()

@app.post("/delete")
async def read_root(params: DeleteParams):
    collection.delete(
        ids=params.ids,
    )
    client.persist()
    return Response(status_code=200)
