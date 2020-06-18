from flask import Flask,json,request

app = Flask(__name__)

@app.route("/hello")
def home():
    return "Welcome Guys, hello "


if  __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
    
