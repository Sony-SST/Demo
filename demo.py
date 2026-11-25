from flask import Flask, request
app=Flask(__name__)
@app.route("/user")
def user():
    name=request.args.get("name")
    return f"hello {name}"


app.run(debug=True)