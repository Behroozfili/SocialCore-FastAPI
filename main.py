from fastapi import FastAPI
from db.database import engine, Base
import db.models as models
from routers import user
from routers import posts
from fastapi.staticfiles import StaticFiles
from typing import List


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory="images"), name="images")

app.include_router(user.router)
app.include_router(posts.router)



@app.get("/")
def  Home():
    return "First page"
