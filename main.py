from flask import Flask, request, redirect
import os
from SQLWrapper import SQLWrapper, DummySQLWrapper
import json
from flask.ext.api.exceptions import APIException, AuthenticationFailed, ParseError

app = Flask(__name__)
sql = DummySQLWrapper()
 
@app.route("/test", methods=['GET', 'POST'])
def hello_monkey():
    return "ayyyy it works"
@app.route("/login", methods=['GET', 'POST'])
def login():
    uname = request.args.get("username")
    password = request.args.get("password")
    try:
        return sql.login(uname, password)
    except:
        raise AuthenticationFailed()
    return "what"
@app.route("/logout", methods=['POST'])
def logout():
    sql.logout(request.args.get("token"))
@app.route("/checkOut", methods=["POST"])
def checkOut():
    objId = request.args.get("objId")
    toId = request.args.get("toId")
    percent = request.args.get("percent")
    loginToken = request.args.get("loginToken")
    sql.checkOut(objId, toId, percent, loginToken)
@app.route("/search/<name>", methods=["GET", "POST"])
def searchByName(name):
    return json.dumps(sql.searchByName(name))
@app.route("/item/<name>", methods=["GET", "POST"])
def search(name):
    return json.dumps(sql.getInfoById(name))
@app.route("/history", methods=["GET", "POST"])
def getHistory():
    num = request.args.get("number")
    if num is None:
        num = -1
    return json.dumps(sql.getHistory(num))
@app.route("history/obj/<name>", methods=["GET", "POST"])
def itemHistory(name):
    num = request.args.get("number")
    if num is None:
        num = -1
    return json.dumps(sql.getHistoryByIteM(name,num))
@app.route("history/user/<name>", methods=["GET", "POST"])
def userHistory(name): 
    num = request.args.get("number")
    if num is None:
        num = -1
    return json.dumps(sql.getHistoryByUser(name,num))
@app.route("history/location/<name>", methods=["GET", "POST"])
def locHistory(name):
    num = request.args.get("number")
    if num is None:
        num = -1
    return json.dumps(sql.getHistoryByCheckoutLocation(name,num))
@app.route("user/list", methods=["POST"])
def getUsers():
    if not sql.checkToken(request.args.get("token")):
        return "waaaat"
    return json.dumps(sql.allUsers())
@app.route("user/info/<user>", methods=["POST"])
def getUser(user):
    if not sql.checkToken(request.args.get("token")):
        return "waaaat"
    return json.dumps(sql.userInfo(user))

if __name__ == "__main__":
    app.run("0.0.0.0",
            8080,
            debug=True)
