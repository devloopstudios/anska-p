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

        self.defaultEmptyValue = "nullbot"
    
    def readRequest(self):
        self.requestValue = jsonLib.getValue(self.fileInput,self.fieldInput,self.defaultEmptyValue)

    def requestTypeSearch(self):
        self.requestType = jsonLib.getColumnByData(self.fileRequest,self.requestValue,self.defaultEmptyValue) 
    
    def replySearch(self):
        self.replyValue = jsonLib.getValue(self.fileReply,self.requestType,self.defaultEmptyValue)  

    def process(self):
        print("hello world")  


        

print(jsonLib.getValue('../input/input.json','text','nothing here'));

jsonLib.setValue('../output/output.json','text','hi');


