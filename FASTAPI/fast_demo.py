from fastapi import FastAPI
app=FastAPI()
employee=[]
@app.get("/employee")
def get_employee():
    return employee
@app.post("/employee")
def add_employee(emp:dict):
    employee.append(emp)
    return {
        "message":"added",
        "employee":emp
    }
@app.put("/employee/{id}")
def update_employee(id:int, data:dict):
    for emp in employee:
        if emp["id"]==id:
            emp["name"]=data["name"]
            return{
                "message":"updated",
                "employee":emp
            }
        return{
            "message":"Not found"
        }

@app.delete("/employee/{id}")
def delete_employee(id:int):
    for emp in employee:

        if emp["id"]==id:
            employee.remove(emp)
            return{
                "message":"deleted",
                "employee":emp
            }
        return{
            "message":"Not found"
        }
