from app.models.posts.post_model import Genre, Post, PostGenres
from app.config import settings
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
from app.schemas.posts import PostCreateSchema
from app.schemas.genres import GenreCreateSchema
from app.routes.posts import router
from fastapi import FastAPI

from datetime import date

@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

app = FastAPI()

app.include_router(router)




# create_genre('Детектив')
# create_genre('Ужасы')
# create_genre('Фантастика')
# # delete_genre('Детектив')
# dedectiv = Genre.get(Genre.title == 'Детектив')
# create_post('godzila', 'new', '1999', 'japan', 'Детектив')
# create_post(title='godzila', county='fj', description='new', year='1999')
# create_post('king-kong', 'new version', '2000', 'USA', ['Фантастика', 'Ужасы'])
# create_post('kayp bulak', 'jany kino', '2007', 'Kyrgyzstan', ['Фантастика', 'Ужасы'])
# print(get_all_films())
# create_post(PostCreateSchema(title='Kok Salkin', description='Jany Kino', year=date(2007, 1, 1), country='Kyrgyzstan', genre=['Ужасы']))
# print(get_film_by_id(1))
# create_genre(GenreCreateSchema(title='Комедия'))
# print(get_genres())

# TODO: дописать CRUD для модели Post
# TODO: ознакомиться с документацией FastAPI