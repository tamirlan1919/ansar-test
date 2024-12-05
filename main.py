from models import User
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def start():
    return {'Hello': 'world'}


@app.post('/user')
async def cmd_handler(user: User):
    if user.age >= 18:
        data_dict = user.dict()
        data_dict.update({'is_adult': True})
        return {
            'message': 'User registered successfully', 'user': data_dict
        }
    else:
        return {
            'message': 'User registered successfully', 'user': user
        }
