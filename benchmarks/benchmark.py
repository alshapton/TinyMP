from tinydb import TinyDB, Query, Storage

import time

import msgpack
from tinymp import *

import os


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def dbins(db):
    db.insert({'type': 'apple', 'count': 7})


def insertstuff(db, n, method, file_name):
    t0 = time.time()
    for i in range(n):
        dbins(db)
    t1 = time.time()

    print method
    print "Write Time: = " + repr(t1 - t0) + "s"
    print file_size(file_name)


db1 = TinyDB('data.json')
db2 = TinyDB('data.msgpack.msg', storage=MsgPackStorage)
db3 = TinyDB('data.umsgpack.msg', storage=MsgPackStorage, Lib='umsgpack')


insertstuff(db1, 1000, 'JSON', 'data.json')
insertstuff(db2, 1000, 'MsgPack', 'data.msgpack.msg')
insertstuff(db3, 1000, 'U-MsgpPack', 'data.umsgpack.msg')

db1.purge_tables()
db2.purge_tables()
db3.purge_tables()
