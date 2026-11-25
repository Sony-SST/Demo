from flask import Flask,request
app=Flask(__name__)
@app.route("/login",methods=["POST"])
def login():
    username=request.json["username"]
    password=request.json["password"]
    if username=="Sony" and password=="Goal@234":
        return {"message":"login success"}
    
    return {"message":"Invalid Login"}
app.run(debug=True)