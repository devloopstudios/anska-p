import json, random

class JsonManager():

    def getValue(path, field, default):

        value = None
        try:    
            with open(path, 'r') as file:
                jsonFile = json.load(file)  

            value = format(jsonFile[field])
        except:
            return default

        if (value is None):        
            return  default
        else:
            return value

    def getValueFromList(path, field, default, position):

        value = None
        try:    
            with open(path, 'r') as file:
                jsonFile = json.load(file)  

            value = jsonFile[field]
        except:
            return default

        if isinstance(value, list):        
            if (position == -1):
                position = random.randint(0,len(value)-1)
            return value[position]    
        else:
            return default

    def getColumnByData(path, value, default):

        jsonFile = open(path, 'r')

        values = json.load(jsonFile)

        jsonFile.close()

        for key, data in values.iteritems():
           if value in data:
               return key

        return default   


    def setValue(path, field, value):

        jsonFile = None

        with open(path, 'r') as file:
            jsonFile = json.load(file) 
            jsonFile[field] = value

        with open(path, 'w') as file:      
            json.dump(jsonFile, file)
