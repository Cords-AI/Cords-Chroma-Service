from pydantic import BaseModel


class SearchBody(BaseModel):
    ids: str | None = None
