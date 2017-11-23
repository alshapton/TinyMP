#!/bin/sh

echo "import msgpack" >> conftest.py
echo "import .tinymp" >> conftest.py

sed -i -e '/import/!s/JSONStorage/MsgPackStorage/g' *.py
sed -i -e '/import/!s/JSON/MsgPack/g' *.py
sed -i -e '/import/!s/json/MsgPack/g' *.py


echo "import msgpack" >> test_storages.py
echo "from .tinymp import *" >> test_storages.py

echo "import msgpack" >> test_middlewares.py
echo "from .tinymp import *" >> test_middlewares.py
