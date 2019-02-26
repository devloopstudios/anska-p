import jsonManagerClass
import expressionParserClass

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
        self.command = ''
        self.useCommand = False

        self.positionListValue = -1
        
        self.jsonManager = jsonManagerClass.JsonManager()
    
    def __del__(self):
        del self.jsonManager

    def setCommand(self, command):
        self.command = command
        self.useCommand = True
        
    def readRequest(self):
        if (not self.useCommand):
            self.requestValue = self.jsonManager.getValue(self.fileInput, self.fieldInput, self.defaultEmptyValue)
        else:
            self.requestValue = self.command

    def requestTypeSearch(self):
        self.requestType = self.jsonManager.getColumnByData(self.fileRequest, self.requestValue, self.defaultEmptyValue) 
    
    def replySearch(self):
        self.replyValue = self.jsonManager.getValueFromList(self.fileReply, self.requestType, self.defaultEmptyValue, self.positionListValue)  

    def replyWrite(self):
        self.jsonManager.setValue(self.fileOutput, self.fieldOutput, self.replyValue)
    
    def expressionValidator(self):
        expressionParser = expressionParserClass.ExpressionParser()  
        self.replyValue = expressionParser.recognize(self.replyValue)
        del expressionParser

    def process(self):

        self.readRequest() 
        self.requestTypeSearch()
        self.replySearch()
        self.expressionValidator()
        self.replyWrite()
        if (self.useCommand):
            print(self.replyValue)
        else:
            print(self.messageFinish)
