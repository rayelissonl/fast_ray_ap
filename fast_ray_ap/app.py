from http import HTTPStatus

from fastapi import FastAPI

from fast_ray_ap.schemas import UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/')
def read_root():
    return {'messsage': 'Ola Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)  # (2)!

    database.append(user_with_id)

    return user_with_id
