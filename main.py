from flask import Flask, request, redirect
import os
from SQLWrapper import SQLWrapper, InvalidIdException, InvalidLoginException
import json

app = Flask(__name__)
sql = SQLWrapper()
 
@app.route("/test", methods=['GET', 'POST'])
def hello_monkey():
    return "ayyyy it works"
@app.route("/brew/coffee", methods=['GET', 'POST'])
def teapot():
    return "I'm a bloody teapot", 418
@app.route("/login", methods=['POST'])
def login():
    uname = request.args.get("username")
    password = request.args.get("password")
    if not isinstance(uname, str) or not isinstance(uname, str):
        return "waaaaaaaaat", 401
    try:
        return sql.login(uname, password)
    except:
        return "wat", 418
@app.route("/logout", methods=['POST'])
def logout():
    token = request.args.get("token")
    if not isinstance(token, str):
        return "that's no token", 404
    sql.logout(token)
@app.route("/checkOut", methods=["POST"])
def checkOut():
    objId = request.args.get("objId")
    toId = request.args.get("toId")
    percent = request.args.get("percent")
    loginToken = request.args.get("loginToken")
    if not isinstance(objId, str) or not isinstance(toId, str) or not isinstance(percent, str) or not isinstance(loginToken, str):
        return "you done screwed up boy", 400
    try:
        sql.checkOut(objId, toId, percent, loginToken)
    except InvalidIdException:
        return "That don't exist", 404
    except InvalidLoginException:
        return "You can't. You just can't", 401
@app.route("/search/<name>", methods=["GET", "POST"])
def searchByName(name):
    return json.dumps(sql.searchByName(name))
@app.route("/item/<name>", methods=["GET", "POST"])
def search(name):
    try:
        return json.dumps(sql.getInfoById(int(name)))
    except InvalidIdException:
        return "Ain't nobody here but us chickens", 404
    except ValueError:
        return "That... is not a number.", 400
@app.route("/history", methods=["GET", "POST"])
def getHistory():
    num = request.args.get("number")
    if not isinstance(num,int):
        num = -1
    return json.dumps(sql.getHistory(num))
@app.route("/history/obj/<name>", methods=["GET", "POST"])
def itemHistory(name):
    num = request.args.get("number")
    if not isinstance(num,int):
        num = -1
    try:
        return json.dumps(sql.getHistoryByIteM(name,num))
    except InvalidIdException:
        return "That's no valid id!", 404
@app.route("/history/user/<name>", methods=["GET", "POST"])
def userHistory(name): 
    num = request.args.get("number")
    if not isinstance(num,int):
        num = -1
    try:
        return json.dumps(sql.getHistoryByUser(name,num))
    except:
        return "I'm sorry, but the person you have requested has a voicemail box not set up yet.", 404
@app.route("/history/location/<name>", methods=["GET", "POST"])
def locHistory(name):
    num = request.args.get("number")
    if not isinstance(num,int):
        num = -1
    try:
        return json.dumps(sql.getHistoryByCheckoutLocation(name,num))
    except InvalidIdException:
        return "Where are we again?", 404
@app.route("/user/list", methods=["POST"])
def getUsers():
    token = request.args.get("token")
    if not isinstance(token, str):
        return "you wot mm8", 400
    if not sql.checkToken(token):
        return "you can't do that!", 401
    return json.dumps(sql.allUsers())
@app.route("/user/info/<user>", methods=["POST"])
def getUser(user):
    token = request.args.get("token")
    if not isinstance(token, str):
        return "you wot mm8", 400
    if not sql.checkToken(token):
        return "you can't do that!", 401
    try:
        return json.dumps(sql.userInfo(int(user)))
    except ValueError:
        return "you wot mm8", 400
    
@app.route("/user/search/<user>", methods=["POST"])
def searchUser(user):
    token = request.args.get("token")
    if not isinstance(token, str):
        return "you wot mm8", 400
    if not sql.checkToken(token):
        return "you can't do that!", 401
    return json.dumps(sql.searchUsers(user))

#if __name__ == "main":
app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)), debug=True)
