from pydantic import BaseModel
from typing import List


class PostParams(BaseModel):
    ids: List[str]
    documents: List[str]
