.. image:: artwork/tinymplogo.png
    :scale: 100%
    :height: 150px
    
.. image:: https://travis-ci.org/alshapton/TinyMP?branch=master
.. image:: https://snyk.io/test/github/alshapton/tinydb-msgpack/badge.svg
.. image:: https://codecov.io/gh/alshapton/TinyMP/branch/master/graph/badge.svg



TinyMP is a storage backend for TinyDB https://github.com/msiemens/tinydb which is based around the MessagePack compressed JSON format (https://msgpack.org/index.html)   

Example Usage:
==============

.. code:: python


    from tinydb import TinyDB, Query,Storage

    import msgpack
    from tinymp import *

    db = TinyDB('data.msg',storage=MsgPackStorage)
    
    def dbins():
       db.insert({'type': 'apple', 'count': 7})
    
    dbins()


As you can see, it's a simple drop-in replacement for any storage engine
and it can be nested and cached.

References:
===========

* TinyDB      https://github.com/msiemens/tinydb 
* MessagePack https://msgpack.org/index.html

