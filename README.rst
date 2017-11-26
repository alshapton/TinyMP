.. image:: artwork/tinymplogo.png
    :scale: 100%
    :height: 150px
    
.. image:: https://travis-ci.org/alshapton/TinyMP.svg?branch=master
.. image:: https://snyk.io/test/github/alshapton/tinydb-msgpack/badge.svg
.. image:: https://codecov.io/gh/alshapton/TinyMP/branch/master/graph/badge.svg



TinyMP is a storage backend for TinyDB https://github.com/msiemens/tinydb which is based around the MessagePack compressed JSON format (https://msgpack.org/index.html)   

Example Usage:
==============

.. code:: python

    from tinydb import TinyDB, Query
    from tinymp import *

    db = TinyDB('data.msg',storage=MsgPackStorage)
    
    def dbins():
       db.insert({'type': 'apple', 'count': 7})
    
    dbins()

As you can see, it's a simple drop-in replacement for any storage engine
and it can be nested and cached.

Why would I use this?
=====================
Looking at the statistics below, it's apparent that compared to the "standard"
JSON Storage mechanism, MessagePack isn't as quick, however, the filesizes on
disc are smaller - consider the table below, with 1,000 JSON documents of 
minute size - clearly, the MessagePack compressed format is smaller than
the JSON format. Whether you choose the default MsgPack library, which is 
marginally slower than the U-MsgPack library (at the cost of a small increase
in storage footprint with U-MsgPack) is dependent on your use case.

'''
  Run #1                             Run #2                Run #3   

JSON                       
  Write Time: = 2.147171974182129s   2.0117878913879395s   2.0401060581207275s
  File Size:  = 37.0 KB              37.0 KB               37.0 KB            

MsgPack
  Write Time: = 9.562603950500488s   9.7328492474328474s   9.716863870620728s
  File Size:  = 21.1 KB              21.1 KB               21.1 KB

U-MsgpPack
  Write Time: = 9.354284048080444s   9.066617012023926s    8.94924020767212s
  File Size:  = 24.1 KB              24.1 KB               24.1 KB
'''

Example Usage using alternative MessgaePack Library:
====================================================

.. code:: python

    from tinydb import TinyDB, Query
    from tinymp import *

    db = TinyDB('data.msg',storage=MsgPackStorage,Lib='umsgpack')
    
    def dbins():
       db.insert({'type': 'apple', 'count': 7})
    
    dbins()

As you can see, it's a simple drop-in replacement for any storage engine
and it can be nested and cached.
Changes
=======

* Version 1.0.0-Beta4 - xx/xx/2017

* Version 1.0.0-Beta3 - 24/11/2017
    * Added support for u-msgpack-python alternative msgpack library

* Version 1.0.0-Beta2 - 11/21/2017
    * Fixed Testing issues

* Version 1.0.0-Beta - 11/19/2017
    * Tidied up repo ready for Beta release

* Version 0.2.0 - 11/18/2017
    * Tidied up repo
    * Added initial benchmarking and example
    * Added Github Community files.

* Version 0.1 - 11/13/2017
    * Initial Release.

References:
===========

* TinyDB      https://github.com/msiemens/tinydb 
* MessagePack https://msgpack.org/index.html

