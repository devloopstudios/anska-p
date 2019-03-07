#save the user request to use it later

class requestSave:

    def __init__(self, connection):
        import MySQLdb
        self._connection = connection;
    
    def execute(self, message):

        result = ""

        return result