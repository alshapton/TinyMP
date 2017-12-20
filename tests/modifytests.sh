#!/bin/sh

# Make a new directory for working
#mkdir originaltests

# Copy ALL tests and duplicate them for both messagepack tests
#copy test*py originaltests

# Create new copies of the Python scripts for each StorageClass subtype
#ls -1  test*.py| awk 'BEGIN     { FS = "." } { print "cp " $0 " " $1".msgpack.py; cp "$0 " " $1 ".umsgpack.py"  }' 

# from future import absolute_import


echo "import umsgpack as msgpack" >> conftest.py
echo "import tinymp" >> conftest.py

sed -i -e '/import/!s/JSONStorage/MsgPackStorage/g' *.py
sed -i -e '/import/!s/JSON/MsgPack/g' *.py
sed -i -e '/import/!s/json/MsgPack/g' *.py


echo "import umsgpack as msgpack" >> test_storages.py
echo "from tinymp import *" >> test_storages.py

echo "import umsgpack as msgpack" >> test_middlewares.py
echo "from tinymp import *" >> test_middlewares.py
