from fastapi import FastAPI
import mysql.connector

app=FastAPI()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Goal@234",
    database="company_db"
)
cursor=conn.cursor()
@app.get("/")
def home():
    return{
        "message":"FASTAPI CRUD"
    }
@app.post("/employee")
def add_emp(emp:dict):
    cursor.execute("insert into employee values(%s,%s,%s,%s)",
                   (
                       emp["id"],
                       emp["name"],
                       emp["department"],
                       emp["salary"]                    ))
    conn.commit()
    return{
        "message":"Employee Added"
    }
@app.get("/employee")
def get_emp():
    cursor.execute("select * from employee")
    return cursor.fetchall()
@app.put("/employee/{id}")
def update_emp(id:int, emp:dict):
    cursor.execute("update employee set salary=%s,department=%s,name=%s where id=%s",
                   (
                       emp["salary"],
                       emp["department"],
                       emp["name"],
                       id
                   ))
    conn.commit()
    return{
        "message":"Updated"
    }
@app.delete("/employee/{id}")
def del_emp(id:int):
    cursor.execute("delete from employee where id=%s",
                   (
                       id,
                   ))
    conn.commit()
    return{
        "message":"deleted"
    }