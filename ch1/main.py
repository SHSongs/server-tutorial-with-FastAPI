from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "hi fast api"
