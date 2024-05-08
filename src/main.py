from dotenv import load_dotenv
load_dotenv()


import uvicorn
import logging, logging.config
from fastapi import FastAPI, Response, HTTPException
from collection import collection, client
from PostParams import PostParams
from DeleteParams import DeleteParams
from SearchBody import SearchBody


LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"default": {"format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s"}},
    "handlers": {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "INFO",
        }
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {"propagate": True},
        "uvicorn.error": {"propagate": True},
    },
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)


app = FastAPI()


@app.post("/search")
async def search(q: str, search_body: SearchBody | None = None):
    where_id = search_body.ids if search_body and search_body.ids else ''

    result = collection.query(
        query_texts=[q],
        n_results=100,
        where={"where_id": where_id},
        include=["distances"]
    )
    return result


@app.post("/")
async def upsert(params: PostParams):
    collection.upsert(
        ids=params.ids,
        documents=params.documents,
    )


@app.post("/delete")
async def delete(params: DeleteParams):
    collection.delete(
        ids=params.ids,
    )
    return Response(status_code=200)


@app.post("/neighbors")
async def embedding(id: str, search_body: SearchBody | None = None):
    where_id = search_body.ids if search_body and search_body.ids else None

    result = collection.get(
            ids=[id],
            include=["embeddings"]
    )

    if not result["embeddings"]:
        raise HTTPException(status_code=400, detail="Invalid id")

    result = collection.query(
        query_embeddings=result["embeddings"],
        n_results=5,
        where={"where_id": where_id},
        include=["distances"]
    )

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
