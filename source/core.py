import readerClass
import sys
import MySQLdb

#realizar refactoring migrando do json para o DB

db = MySQLdb.connect(host="192.168.0.20",    
                     user="mence",        
                     passwd="21021996",  
                     db="anska")       


cur = db.cursor()


cur.execute("SELECT * FROM BOT_REQUEST")


for row in cur.fetchall():
    print row[1] + row[2]

db.close()

#reader = readerClass.Reader()
#if (len(sys.argv) > 1):
#    reader.setCommand(sys.argv[1])
#reader.process()

#del reader


