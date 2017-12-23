
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
        super(MsgPackStorage, self).__init__()
        touch(path, create_dirs=create_dirs)  # Create file if not exists
        self.kwargs = kwargs
        '''
        Import the correct msgpack library
        '''
        if 'Lib' in kwargs:
            self.library = self.kwargs['Lib']

            if self.library == 'umsgpack':
                import umsgpack as msgpack
                self.msgpack = msgpack
            else:
                import msgpack
                self.msgpack = msgpack
        else:
            import msgpack
            self.msgpack = msgpack

        self._handle = open(path, 'r+')

    def write(self, data):
        self._handle.seek(0)
        serialized = self.msgpack.dump(data, self._handle)
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
            return self.msgpack.unpackb(self._handle.read())

    def close(self):
        self._handle.close()
