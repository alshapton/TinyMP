.. image:: artwork/tinymplogo.png
    :scale: 100%
    :height: 150px
    
.. image:: https://travis-ci.org/alshapton/TinyMP.svg?branch=master
.. image:: https://snyk.io/test/github/alshapton/tinydb-msgpack/badge.svg
.. image:: https://codecov.io/gh/alshapton/TinyMP/branch/master/graph/badge.svg
.. image:: https://img.shields.io/badge/code%20style-pep8-orange.svg



TinyMP is a storage backend for TinyDB https://github.com/msiemens/tinydb which is based around the MessagePack compressed JSON format (https://msgpack.org/index.html)   

Syntax :
========
TinyMP extends the syntax of the ``tinydb`` class using one of the optional ``kwargs`` as follows:


.. code:: python
    class tinydb.database.TinyDB(*args, **kwargs)

.. csv-table:: Values for ``**kwargs``
   :header: "Value","Effect"
   :widths: 10,90

   "``storage=MsgPackStorage``","Default option, will use the ``MsgPack`` library"
   "``storage=MsgPackStorage,Lib='msgpack'``","Will use the ``MsgPack`` library"
   "``storage=MsgPackStorage,Lib='umsgpack'``","Will use the ``U-MsgPack`` Library"


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
and it can be nested and cached. Don't forget, you will need to install as a minimum,
the ``msgpack-python`` library using ``pip install msgpack-python`` and the ``U-MsgPack``
library from https://github.com/vsergeev/u-msgpack-python in order to use that option.

Example Usage using alternative MessagePack Library:
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

Why would I use this?
=====================
Looking at the statistics below, it's apparent that compared to the "standard"
JSON Storage mechanism, MessagePack isn't as quick, however, the filesizes on
disc are smaller - consider the table below, with 1,000 JSON documents of 
minute size - clearly, the MessagePack compressed format is smaller than
the JSON format. Whether you choose the default MsgPack library, which is 
marginally slower than the U-MsgPack library (at the cost of a small increase
in storage footprint with U-MsgPack) is dependent on your use case.

.. csv-table:: Timings (seconds)
   :header: "Format","Run 1", "Run 2", "Run 3", "FileSize"
   :widths: 10,30, 30, 30,10 

   "JSON Write:", 2.147,2.011,2.040,"37.0 Kb"
   "MsgPack Write:", 9.562,9.732,9.716,"21.1 Kb"
   "U-MsgPack Write:", 9.354,9.066,8.949,"24.1 Kb"

Changes
=======

* Version 1.0.0-Beta5 - XX/XX/XXXX
    * Added PiPy compatibility 
    * PEP-8 Compliant code style

* Version 1.0.0-Beta4 - 11/26/2017
    * Added descriptions of benchmarking and tidied up repo
    * Further added information to README about usage

* Version 1.0.0-Beta3 - 11/24/2017
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
* U-MsgPack   https://github.com/vsergeev/u-msgpack-python

