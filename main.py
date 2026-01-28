from fastapi import FastAPI
from db.database import engine, Base
import db.models as models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def  Home():
    return "First page"
