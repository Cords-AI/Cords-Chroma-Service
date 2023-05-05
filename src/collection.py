import chromadb
import os
from chromadb.utils import embedding_functions
from USEM_embedding_function import USEMEmbeddingFunction

__all__ = ["collection"]

model_name = "USEM"

embedding_function = USEMEmbeddingFunction()

if "OPENAI_API_KEY" in os.environ and os.environ["OPENAI_API_KEY"] != "":
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    model_name = "text-embedding-ada-002"

    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name=model_name
    )

client = chromadb.Client(
    chromadb.config.Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=f"/data/{model_name}"
    )
)

collection = client.get_or_create_collection(name="cords", embedding_function=embedding_function)
