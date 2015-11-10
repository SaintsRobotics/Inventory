class SQLWrapper:
    #I dunno what you'll need for your constructor
    def _init_(this, fill your stuff):
        pass
    #Check the username and password, then generate the logintoken
    def login(this, username, password):
        return logintoken
    #Delete the Logintoken
    def logout(this, logintoken):
        pass
    #check out an object. Pretty self-explanitory.
    def checkOut(this, objId, toId, percent, loginToken):
        pass
    #Return a list of all the objects represting anything with a lazy string complete (I'll get you some algorithm docs/libraries later)
    def searchByName(this, name):
        return results 
    #Return the info of an object with this ID
    def getInfoById(this, objId}:
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
    def getHistoryByIten(this, itemId, num):
        return history

class InvalidLoginException(Exceptino):
    #yeaaaaah
    pass
