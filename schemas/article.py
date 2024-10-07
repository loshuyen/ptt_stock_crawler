from pydantic import BaseModel

class Article(BaseModel):
    title: str
    rating: int | str | None = None
    date: str

class Articles(BaseModel):
    data: list[Article]