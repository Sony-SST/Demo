from flask import Flask,request,jsonify
app=Flask(__name__)
employee=[]
@app.route("/employee",methods=["POST"])
def add_employee():
    data=request.json
    employee.append(data)
    return jsonify({
        "message":"Employee added succesfully",
        "employee":data
    })
@app.route("/employee",methods=["GET"])
def get_employee():
    return jsonify(employee)
@app.route("/employee/<int:id>",methods=["PUT"])
def employee_update(id):
    for emp in employee:
        if emp["id"]==id:
            emp["name"]=request.json["name"]
            return jsonify({
                "message":"updated",
                "employee":emp
            })
    return jsonify({
        "message":"Employee not found"
    })
@app.route("/employee/<int:id>",methods=["DELETE"])
def employee_delete(id):
    for emp in employee:
        if emp["id"]==id:
            employee.remove(emp)
            return jsonify({
                "message":"Deleted"
            })

    return jsonify({
        "message":"Employee not found"
    })
app.run(debug=True)
