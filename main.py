from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('paitents.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def Hello():
    return {'message': 'Paitent Management System API'}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage our paitents records...'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description='ID of the patient in the DB',example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found!')

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight and bmi'), order: str = Query('acc', description= 'Sort in accending or descending order.')):

    valid_fields = 
