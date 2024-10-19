from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["/users"],
                   responses={404:{"message": "Not found"}})
#Inicia el server: uvicorn users:router --reload

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age:int

users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
         User(id=2, name="Moure",  surname="Dev", url="https://moure.dev", age=35),
         User(id=3, name="Haakoon", surname="Dahberg", url="https://haakon.com", age=33)]

@router.get("/json", response_model= list[User], status_code=201)
async def usersjson():
    return [{"name":"Brais", "surname" : "Moure", "url" : "https://moure.dev", "age": 35},
            {"name":"Moure", "surname" : "Dev", "url" : "https://moure.dev", "age": 35},
            {"name":"Haakoon", "surname" : "Dahberg", "url" : "https://haakon.com", "age": 33}]

@router.get("/", response_model= list[User], status_code=201)
async def users():
    return users_list