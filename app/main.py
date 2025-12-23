from fastapi import FastAPI
from app.database import engine
from app import models

app = FastAPI()

# Create DB tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Mozhii AI Auth Backend is running"}
