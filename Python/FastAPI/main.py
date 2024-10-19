from fastapi import FastAPI
from routers import products, users, user, basic_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#include routers
app.include_router(user.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth_users.router)
app.mount("/static", StaticFiles(directory='static'), name='static')

@app.get("/")
async def root():
    return "Hello World"

@app.get("/json")
async def jsonFile():
    return { "First" : "json" }