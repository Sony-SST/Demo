from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Flask"
@app.route("/about")
def about():
    return "About Page"
'''@app.route("/employee",methods=["GET"])
def employee():
    return {
        "id":1,
        "name":"Sony",
        "Salary":50000
    }
@app.route("/employee",methods=["POST"])
def add_employee():
    data=request.json
    return ({
        "message":"Employee added succesfully",
        "employee":data
    })'''
app.run(debug=True)
