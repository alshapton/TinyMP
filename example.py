from tinydb import TinyDB, Query, Storage

import msgpack
from tinymp import *

db = TinyDB('data.msg', storage=MsgPackStorage, Lib="msgpack")


def dbins():
    db.insert({'type': 'apple', 'count': 7})


dbins()
