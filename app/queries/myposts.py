from app.models.posts.post_model import Post, PostGenres
from app.models.posts.post_model import Genre

from app.models.basemodel import db

@db
def create_post(title, description, year, country, genre):
    
    post = Post.create(
        title=title,
        description=description, 
        year=year, 
        country=country
    )

    # huey.courses.add(Course.select().where(Course.name.contains('English')))

    post.genre.add(Genre.select().where(Genre.title == genre))
    return post


def delete_post(title, genre):
    deleted = Post.get(Post.title == title)
    deleted.genre.remove(Genre.select().where(Genre.title.startswith(genre)))
    deleted.delete_instance()


def get_post():
    return [post.title for post in Post.select()]
# TODO: написать CRUD для модели Posts