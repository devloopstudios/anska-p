import random
import datetime
import jsonManagerClass

class ExpressionParser():

    def getDateTime(self):
        return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    def getMyName(self):
        jsonManager = jsonManagerClass.JsonManager()
        myName = jsonManager.getValue("../data/config.json","myName","pipoca")
        del jsonManager
        return myName
    
    def getMyBirthdate(self):
        jsonManager = jsonManagerClass.JsonManager()
        myBirthdate = jsonManager.getValue("../data/config.json","myBirthdate","I don't know")
        del jsonManager
        return myBirthdate


    def recognize(self, sentence):

        expressionDictionary = {
            "@datetime" : self.getDateTime,
            "@myName" : self.getMyName,
            "@myBirthdate" : self.getMyBirthdate
        }

        for key, value in expressionDictionary.items():
            if key in sentence:
                sentence = sentence.replace(key, value())

        return sentence