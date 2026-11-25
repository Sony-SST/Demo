from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
employees=[]
class employee(BaseModel):
    id:int
    name:str
    department:str
    salary:float
@app.post("/employee")
def add_emp(emp:employee):
    employees.append(emp.dict())
    return {
        "message":"Added",
        "employee":emp
    }
@app.get("/employee")
def get_emp():
    return employees
@app.put("/employee/{id}")
def update_emp(id:int,emp:employee):
    for i in range(len(employees)):
        if employees[i]["id"]==id:
            employees[i]=emp.dict()
            return{
                "message":"Updated",
                "employee":emp
            }
    return{
        "message":"Employee Not Found"
    }
@app.delete("/employee/{id}")
def delete_emp(id:int):
    for emp in employees:
        if emp["id"]==id:
            employees.remove(emp)
            return{
                "message":"Deleted",
                "employees":emp
            }

    return{
        "message":"Employee not Found"
    }
