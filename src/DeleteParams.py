from pydantic import BaseModel
from typing import List

class DeleteParams(BaseModel):
    ids: List[str]
