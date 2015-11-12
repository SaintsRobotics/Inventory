class SQLWrapper:
    #I dunno what you'll need for your constructor
    def _init_(this, fill_your_stuff):
        pass
    #Check the username and password, then generate the logintoken
    #The password passed is the hashed uesr password. The password stored should be that hashed.
    def login(this, username, password):
        return logintoken
    def checkToken(this,token):
        return bool
    #Delete the Logintoken
    def logout(this, logintoken):
        pass
    #check out an object. Pretty self-explanitory.
    def checkOut(this, objId, toId, percent, loginToken):
        pass
    #Return a list of all the objects containing this string
    def searchByName(this, name):
        return results
    #Return the info of an object with this ID
    def getInfoById(this, objId):
        return result
    #Return all history, going back num transactions (-1 for all)
    def getHistory(this, num):
        return history
    #Get all the history from a given user, going back num transactions (-1 for all)
    def getHistoryByUser(this, userId, num):
        return history
    #Return all the history for a given checkout Location, going back num transactions(-1 for all)
    def getHistoryByCheckoutLocation(this, locId, num):
        return history
    #Return all the history for a given item, going back num transactiosn (-1 for all)
    def getHistoryByIteM(this, itemId, num):
        return history
    #return a listing of all users and their names
    def allUsers(this):
        return allUser
    #info for one user
    def userInfo(this, user):
        return user
        
class InvalidLoginException(Exception):
    #yeaaaaah
    pass
class InvalidIdException(Exception):
    pass

class DummySQLWrapper:
    #I dunno what you'll need for your constructor
    def _init_(this):
        pass
    #Check the username and password, then generate the logintoken
    #The password passed is the hashed uesr password. The password stored should be that hashed.
    def login(this, username, password):
        return {username:password}
    def checkToken(this,token):
        return True
    #Delete the Logintoken
    def logout(this, logintoken):
        pass
    #check out an object. Pretty self-explanitory.
    def checkOut(this, objId, toId, percent, loginToken):
        pass
    #Return a list of all the objects containing this string
    def searchByName(this, name):
        return {"ayyyy" : name}
    #Return the info of an object with this ID
    def getInfoById(this, objId):
        return {"blazeit" : objId}
    #Return all history, going back num transactions (-1 for all)
    def getHistory(this, num):
        return {"Black" : num}
    #Get all the history from a given user, going back num transactions (-1 for all)
    def getHistoryByUser(this, userId, num):
        return {"Becker" : str(userId) +"APWH"+ str(num)}
    #Return all the history for a given checkout Location, going back num transactions(-1 for all)
    def getHistoryByCheckoutLocation(this, locId, num):
        return {"Olivera" : str(locId) + "APUSH" + str(num)}
    #Return all the history for a given item, going back num transactiosn (-1 for all)
    def getHistoryByIteM(this, itemId, num):
        return {"Now the party dont start": str(itemId) + "Till I walk in" + str(num)}
    #return a listing of all users and their names
    def allUsers(this):
        return {"Everybody dance now" : "Everybody, rock your body"}
    #info for one user
    def userInfo(this, user):
        return {"dun, dun, dun dun dun " : user }
