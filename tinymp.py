
import msgpack
from tinydb import Storage

class MsgPackStorage(Storage):
    def __init__(self, filename):  
        self.filename = filename

    def read(self):
        try:
            open(self.filename)
        except IOError:
            return None 

        with open(self.filename) as handle:
            try:
                data = msgpack.unpackb(handle.read()) 
                return data
            except IOError:
                return None 

    def write(self, data):
        with open(self.filename, 'w') as handle:
            msgpack.dump(data, handle)

    def close(self): 
        pass
