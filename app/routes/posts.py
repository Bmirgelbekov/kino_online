from app.queries.posts import get_all_films, get_film_by_id, create_post
from app.schemas.posts import PostCreateSchema

from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def get_films():
    return get_all_films()

@router.post('/create-post')
def creage_film(film: PostCreateSchema):
    return create_post(film)

# @router.delete('/delete-post')


# TODO: Дописать пути для остльных функций