from fastapi import FastAPI
from db.database import engine, Base
import db.models as models
from routers import user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)


@app.get("/")
def  Home():
    return "First page"
