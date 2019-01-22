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

    
    def readRequest(self):
        self.requestValue = jsonLib.getValue(self.fileInput, self.fieldInput, self.defaultEmptyValue)

    def requestTypeSearch(self):
        self.requestType = jsonLib.getColumnByData(self.fileRequest, self.requestValue, self.defaultEmptyValue) 
    
    def replySearch(self):
        self.replyValue = jsonLib.getValueFromList(self.fileReply, self.requestType, self.defaultEmptyValue, self.positionListValue)  

    def replyWrite(self):
        jsonLib.setValue(self.fileOutput, self.fieldOutput, self.replyValue)

    def process(self):
        self.readRequest() 
        self.requestTypeSearch()
        self.replySearch()
        self.replyWrite()
        print(self.messageFinish)

reader = Reader()
reader.process()


