from tinydb import TinyDB, Query,Storage

import msgpack
from tinydb-msgpack import *

db = TinyDB('data2.msg',storage=MsgPackStorage)

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})
