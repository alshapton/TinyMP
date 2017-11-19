from tinydb import TinyDB, Query,Storage

import time

import msgpack
from tinymp import *

db1 = TinyDB('data.msg',storage=MsgPackStorage)
#db1 = TinyDB('data.json')

def dbins1():
   db1.insert({'type': 'apple', 'count': 7})

def dbins2():
   db2.insert({'type': 'apple', 'count': 7})

db1.purge_tables()

n = 1000
t0 = time.time()
for i in range(n): dbins1()
t1 = time.time()

print (t1-t0)
print "Write Benchmark: JSON = " + repr(t1-t0)
