import jsonLib

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
        
        self.jsonManager = JsonManager()
    
    def __del__(self):
        del jsonManager;
        
    def readRequest(self):
        self.requestValue = jsonManager.getValue(self.fileInput, self.fieldInput, self.defaultEmptyValue)

    def requestTypeSearch(self):
        self.requestType = jsonManager.getColumnByData(self.fileRequest, self.requestValue, self.defaultEmptyValue) 
    
    def replySearch(self):
        self.replyValue = jsonManager.getValueFromList(self.fileReply, self.requestType, self.defaultEmptyValue, self.positionListValue)  

    def replyWrite(self):
        jsonManager.setValue(self.fileOutput, self.fieldOutput, self.replyValue)

    def process(self):
        self.readRequest() 
        self.requestTypeSearch()
        self.replySearch()
        self.replyWrite()
        print(self.messageFinish)

reader = Reader()
reader.process()
del reader


