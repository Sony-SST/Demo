from flask import Flask, jsonify, request
app=Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Amit",
        "department": "IT",
        "salary": 30000
    },
    {
        "id": 2,
        "name": "Sneha",
        "department": "HR",
        "salary": 25000
    },
    {
        "id": 3,
        "name": "Rohit",
        "department": "Finance",
        "salary": 35000
    },
    {
        "id": 4,
        "name": "Sakshi",
        "department": "IT",
        "salary": 45000
    },
     {
        "id": 5,
        "name": "Soni",
        "department": "HR",
        "salary": 75000
    }


]

#This is the change


@app.route('/employees', methods=['GET'])
def get_employee():
    return jsonify(employees)
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    for employee in employees:
        if employee['id']==employee_id:
            return jsonify(employee)
    return jsonify({
        "error":"Employee Not Found"
    }
),404
@app.route('/employees', methods=['POST'])
def add_employee():
    data=request.get_json()
    employees.append(data)
    return jsonify({
        "msg":"Employee added succesfully"
    }),201
app.run(debug=True)
