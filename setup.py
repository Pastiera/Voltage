# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "Voltage"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open('requirements.txt') as f:
    REQUIRES = f.read().splitlines()


setup(
    name=NAME,
    version=VERSION,
    description="AC/DC",
    author_email="",
    url="",
    install_requires=REQUIRES,
    packages=find_packages(),
    #package_data={"": ["openapi/openapi.yaml"]},
    #include_package_data=True,
    entry_points={"console_scripts": ["openapi_server=Voltage.Voltage"]},
)
