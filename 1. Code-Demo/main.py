from fastapi import fastapi

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello World'}