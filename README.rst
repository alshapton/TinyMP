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

