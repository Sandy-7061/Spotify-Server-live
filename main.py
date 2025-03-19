from fastapi import FastAPI
from database import engine
from model.base import Base
from routes import auth


app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])


# ✅ Create tables after defining models
Base.metadata.create_all(bind=engine)


# Just Checking if the app is running
@app.get("/")
def read_root():
    return {"message": "Hello World"}

