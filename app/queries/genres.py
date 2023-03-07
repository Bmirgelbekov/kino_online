from peewee import IntegrityError, DoesNotExist

from app.schemas.genres import GenreCreateSchema
from app.models.posts.post_model import Genre
from app.models.basemodel import db


# @db
# def create_genre(title):
#     try:
#         obj = Genre.create(title=title)
#     except IntegrityError:
#         return 0
#     return obj

@db
def create_genre(genre_in: GenreCreateSchema):
    genre = Genre.create(title=genre_in.title)
    return genre


def delete_genre(title):
    try:
        genre = Genre.get(title=title)
        # SELECT * FROM genre WHERE title=title
        genre.delete_instance()
    except DoesNotExist:
        return 0
    return 1

@db
def get_genres():
    return [genre.title for genre in Genre.select()]