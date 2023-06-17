from pydantic import BaseModel

class PostParams(BaseModel):
    id: str
    document: str
