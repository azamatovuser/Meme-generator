from fastapi import FastAPI
import models
from database import engine
from routers import memes_router

app = FastAPI()
app.include_router(memes_router)

models.Base.metadata.create_all(bind=engine)
