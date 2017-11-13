from tinydb import TinyDB, Query,Storage

import time

import msgpack
from tinymp import *

#db = TinyDB('data2.msg',storage=MsgPackStorage)
db = TinyDB('data.json')

def dbins():
   db.insert({'type': 'apple', 'count': 7})

n = 1000
t0 = time.time()
for i in range(n): dbins()
t1 = time.time()

print( t1-t0)
