from fastapi import APIRouter
from config.db import conn
from models.user import details
from schemas.user import User
user = APIRouter()

@user.get('/')
def fetch_users():
    return conn.execute(details.select()).fetchall()

@user.post('/')
def post_user(user: User):
    return conn.execute(details.insert().values(name=user.name,email=user.email,password=user.password))

@user.put('/{id}')
def update_user(id:int ,user:User):
    return conn.execute(details.update().values(name=user.name,email=user.email,password=user.password).where(details.c.id == id))

@user.delete('/{id}')
def delete_user(id: int):
    return conn.execute(details.delete().where(details.c.id == id)).fetchall()