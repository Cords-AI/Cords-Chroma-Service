from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from collection import collection

app = FastAPI()

@app.get("/")
def read_root(q: str):
    result = collection.query(
        query_texts=[q],
        n_results=100,
        include=[]
    )
    return result
