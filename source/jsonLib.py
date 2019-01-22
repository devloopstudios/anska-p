import json

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

def getColumnByData(path, field, default):
    #todo : finish here catching arrays
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


def setValue(path, field, value):

    jsonFile = None

    with open(path, 'r') as file:
        jsonFile = json.load(file) 
        jsonFile[field] = value

    with open(path, 'w') as file:      
        json.dump(jsonFile, file)
