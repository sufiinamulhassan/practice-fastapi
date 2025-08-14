from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('paitents.json', 'r') as f:
        data = json.load(f)
    return 

@app.get("/")
def Hello():
    return {'message': 'Paitent Management System API'}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage our paitents records...'}

@app.get("/view")
def view():
    data = load_data
    return data