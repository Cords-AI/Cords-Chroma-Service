from pydantic import BaseModel

class PostParams(BaseModel):
    id: str
    partner: str
    document: str