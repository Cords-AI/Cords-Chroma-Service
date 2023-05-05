import tensorflow_hub, tensorflow_text
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

class USEMEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        embeds = tensorflow_hub.load("/model")
        embeddings = embeds(texts)
        x_np = embeddings.numpy()
        return x_np
