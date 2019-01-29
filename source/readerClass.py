import jsonManagerClass

class Reader:
    def __init__(self):
        self.language = 'en_us'

        self.fileInput = '../input/input.json'
        self.fileOutput = '../output/output.json'
        self.fileRequest = '../data/'+self.language+'/request_types.json'
        self.fileReply = '../data/'+self.language+'/reply_types.json'

        self.fieldInput = 'text'
        self.fieldOutput = 'text'

        self.defaultEmptyValue = 'null'
        self.messageFinish = 'Done'

        self.positionListValue = -1
        
        self.jsonManager = jsonManagerClass.JsonManager()
    
    def __del__(self):
        del self.jsonManager
        
    def readRequest(self):
        self.requestValue = self.jsonManager.getValue(self.fileInput, self.fieldInput, self.defaultEmptyValue)

    def requestTypeSearch(self):
        self.requestType = self.jsonManager.getColumnByData(self.fileRequest, self.requestValue, self.defaultEmptyValue) 
    
    def replySearch(self):
        self.replyValue = self.jsonManager.getValueFromList(self.fileReply, self.requestType, self.defaultEmptyValue, self.positionListValue)  

    def replyWrite(self):
        self.jsonManager.setValue(self.fileOutput, self.fieldOutput, self.replyValue)

    def process(self):
        self.readRequest() 
        self.requestTypeSearch()
        self.replySearch()
        self.replyWrite()
        print(self.messageFinish)
