from fastapi import FastAPI

app = FastAPI(title="My Music Platform")


@app.get("/")
def index():
    return {"message": "Привет, музыкальная площадка!"}