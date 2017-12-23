# coding=utf-8
from distutils.util import convert_path
from setuptools import setup, find_packages
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


# This will set the version string to __version__
__version__ = '1.0.0-Beta5'


setup(
    name="tinymp",
    version=__version__,
    packages=find_packages(),

    # development metadata
    zip_safe=True,

    # metadata for upload to PyPI
    author="Andrew Shapton",
    author_email="alshapton@gmail.com",
    description="TinyMP is a MessagePack Storage extension for the TinyDB database https://github.com/msiemens/tinydb",
    license="MIT",
    keywords="database nosql python tinydb documentdb",
    url="https://github.com/alshapton/TinyMP/",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ],

    long_description=read('README.rst'),
)
