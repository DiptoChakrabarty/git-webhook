from flask import Flask,json,request

app = Flask(__name__)


@app.route("/github",methods=["POST"])
def git_post():
    if request.headers["Content-Type"] == "application/json":
        print(json.dumps(request.json))
        return json.dumps(request.json)



if  __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
