from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Response
from collection import collection, client
from PostParams import PostParams
from DeleteParams import DeleteParams
from SearchBody import SearchBody

app = FastAPI()


@app.post("/search")
async def search(q: str, search_body: SearchBody | None = None):
    where_id = search_body.ids if search_body and search_body.ids else None

    result = collection.query(
        query_texts=[q],
        n_results=100,
        where_id=where_id,
        include=[]
    )
    return result


@app.post("/")
async def upsert(params: PostParams):
    collection.upsert(
        ids=[params.id],
        metadatas=[{"partner": params.partner}],
        documents=[params.document],
    )
    client.persist()


@app.post("/delete")
async def delete(params: DeleteParams):
    collection.delete(
        ids=params.ids,
    )
    client.persist()
    return Response(status_code=200)
