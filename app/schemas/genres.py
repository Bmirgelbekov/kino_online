# TODO: Написать схемы для жанров
from pydantic import BaseModel


class GenreCreateSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True

