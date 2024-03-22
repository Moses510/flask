from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello, world"

@app.route("/moses")
def name():
    return "my name is moses"

@app.route("/team")
def team():
    return "my project team members are Prakash, Raju, Ravi, Teja, Mayi, Baby"

@app.route("/add")
def add():
    a = 1+1
    return "addition of 1 + 1 is {}".format(a)

@app.route("/input")
def input():
    data = request.args.get('x')
    return "this is my first url input {}".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")

