try:
    import umsgpack as msgpack
except ImportError:
    import msgpack

from tinydb import Storage

import os

def touch(fname, create_dirs):
    if create_dirs:
        base_dir = os.path.dirname(fname)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    with open(fname, 'a'):
        os.utime(fname, None)

class MsgPackStorage(Storage):
    def __init__(self, path, create_dirs=False, **kwargs):
        #self.filename = filename
        super(MsgPackStorage, self).__init__()
        touch(path, create_dirs=create_dirs)  # Create file if not exists
        self.kwargs = kwargs
        self._handle = open(path, 'r+')


    def write(self, data):
        self._handle.seek(0)
        serialized = msgpack.dump(data, self._handle)
        #self._handle.write(serialized)
        self._handle.flush()
        self._handle.truncate()


    def read(self):
        # Get the file size
        self._handle.seek(0, os.SEEK_END)
        size = self._handle.tell()

        if not size:
            # File is empty
            return None
        else:
            self._handle.seek(0)
            return  msgpack.unpackb(self._handle.read()) 


    def close(self):
        self._handle.close()
