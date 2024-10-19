from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/user",
                   tags=["/user"],
                   responses={404:{"message": "Not found"}})

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age:int

users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
         User(id=2, name="Moure",  surname="Dev", url="https://moure.dev", age=35),
         User(id=3, name="Haakoon", surname="Dahberg", url="https://haakon.com", age=33)]

#Url by path 
@router.get("/{id}", response_model= User, status_code=status.HTTP_200_OK)
async def user(id: int):
    return search_user(id)
    
#Url by query    
@router.get("/", response_model= User, status_code=status.HTTP_200_OK)
async def user(id: int):
    return search_user(id)

@router.post("/", response_model= User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "User already exists")
    else:
        users_list.routerend(user)
        return user

@router.put("/", response_model= User, status_code=status.HTTP_201_CREATED)
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "User does not exists")

    return user

@router.delete("/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "User does not exists")

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "User does not exists")