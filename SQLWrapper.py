from peewee import *
import _mysql
import string
import random
import itertools
import datetime

db = MySQLDatabase('mysql', user="root", charset="utf8mb4")

class BaseModel(Model):
    class Meta:
        database = db
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    login_token = CharField(unique=True)
class Location(BaseModel):
    common_name = CharField()
    description = TextField()
class Item(BaseModel):
    common_name = CharField()
    current_user = ForeignKeyField(User, to_field="id", related_name="checkouts")
    storage_location = ForeignKeyField(Location, to_field="id", related_name="contents")
    percentage_left = IntegerField()
class Transaction(BaseModel):
    item = ForeignKeyField(Item, to_field="id", related_name="transactions")
    user = ForeignKeyField(User, to_field="id", related_name="transactions")
    time = DateTimeField(default=datetime.datetime.now)
    percent_left = IntegerField()

class SQLWrapper:
    #I dunno what you'll need for your constructor
    def _init_(self):
        pass
    def dictionarifyUser(self, user):
        result = {}
        result["id"] = user.id
        result["first_name"] = user.first_name
        result["last_name"] = user.last_name
        result["email"] = user.email
        return result
    def dictionarifyItem(self, item):
        result = {}
        result["id"] = item.id
        result["common_name"] = item.common_name
        result["current_user"] = item.current_user
        result["storage_location"] = item.storage_location
        result["percentage_left"] = item.percentage_left
        return result
    def dictionarifyTransaction(self, transac):
        result = {}
        result["item"] = transac.item
        result["user"] = transac.user
        result["time"] = transac.time
        result["percent_left"] = transac.percent_left
        return result
    def filterTransactionList(self, num, history):
        if num >= 0 and num < history.count():
            sliced = itertools.islice(history, num)
        else:
            sliced = history
        result = {}
        i = 0
        for transac in sliced:
            result[i] = dictionarifyTransaction(transac)
            i += 1
        return result
    #Check the username and password, then generate the logintoken
    #The password passed is the hashed uesr password. The password stored should be that hashed.
    def login(self, username, password):
        db.connect()
        loginuser = db.User.get(User.username==username, User.password==password)
        gentoken = ''.join(random.choice(string.ascii_uppercase) for i in range(15))
        loginuser.update(login_token=gentoken).execute()
        db.close()
        return gentoken
    #check if the token matches the one in the db
    def checkToken(self, username, token):
        db.connect()
        try:
            db.User.get(User.username == username, User.login_token==token)
            valid = True
        except:
            valid = False
        db.close()
        return valid
    #Delete the Logintoken
    def logout(self, logintoken):
        db.connect()
        loginuser = db.User.get(User.login_token==logintoken)
        loginuser.update(login_token='').execute()
        db.close()
        pass
    #check out an object. Pretty self-explanitory.
    def checkOut(self, objId, toId, percent, loginToken):
        db.connect()
        if db.User.get(User.login_token==loginToken).id==toId:
            transac = db.Transaction.create(item=objId, user=toId, percent_left=percent)
            item = db.Item.select().where(Item.id==objId)
            item.update(current_user=transac.user, percentage_left=transac.percent_left).execute()
        db.close()
        pass
    #Return a list of all the objects containing this string
    #Format {index, object}
    def searchByName(self, name):
        i = 0
        result = {}
        db.connect()
        search = db.Item.select().where(name in Item.common_name)
        for item in search:
            result[i] = dictionarifyItem(item)
            i += 1
        db.close()
        return result
    #Return the info of an object with this ID
    def getInfoById(self, objId):
        db.connect()
        result = dictionarifyItem(db.Item.select().where(Item.id == objId))
        db.close()
        return result
    #Return all history, going back num transactions (-1 for all)
    def getHistory(self, num):
        db.connect()
        history = db.Transaction.search().order_by(Tweet.time.desc())
        db.close()
        return filterTransactionList(num, history)
    #Get all the history from a given user, going back num transactions (-1 for all)
    def getHistoryByUser(self, userId, num):
        db.connect()
        history = db.User.get(User.id == userId).transactions
        db.close()
        return filterTransactionList(num, history)
    #Return all the history for a given checkout Location, going back num transactions(-1 for all)
    def getHistoryByCheckoutLocation(self, locId, num):
        db.connect()
        history = db.Location.get(Location.id == locId).transactions
        db.close()
        return filterTransactionList(num, history)
    #Return all the history for a given item, going back num transactiosn (-1 for all)
    def getHistoryByItem(self, itemId, num):
        db.connect()
        history = db.Item.get(Item.id == itemId).transactions
        db.close()
        return filterTransactionList(num, history)
    #return a listing of all users and their names
    def allUsers(self):
        db.connect()
        userlisting = db.User.select()
        db.close()
        result = {}
        i = 0
        for user in userlisting:
            result[i] = dictionarifyUser(user)
            i += 1
        return result
    #info for one user. Input is ID
    def userInfo(self, user):
        db.connect()
        user = db.User.get(User.id == user)
        db.close()
        return {0:dictionarifyUser(user)}

class InvalidLoginException(Exception):
    #yeaaaaah
    pass

class InvalidIdException(Exception):
    pass