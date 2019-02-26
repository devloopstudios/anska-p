import readerClass
import sys

reader = readerClass.Reader()
if (len(sys.argv) > 1):
    reader.setCommand(sys.argv[1])
reader.process()

del reader


