# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "cybersource-rest-client-python"
VERSION = "0.0.14"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3", "six", "certifi", "DateTime", "Naked", "PyJWT", "PyNaCl", "PyYAML",
            "asn1crypto",
            "bcrypt",
            "certifi",
            "cffi",
            "chardet",
            "extras",
            "fixtures",
            "configparser",
            "crypto",
            "cryptography",
            "enum34",
            "funcsigs",
            "nose",
            "coverage",
            "jsonschema",
            "linecache2",
            "pbr",
            "idna",
            "ipaddress",
            "logger",
            "paramiko",
            "pip",
            "pyOpenSSL",
            "pyasn1",
            "pycparser",
            "pycryptodome",
            "pycryptodomex",
            "pypi",
            "python-mimeparse",
            "python-subunit",
            "python-toolbox",
            "pytz",
            "requests",
            "rsa",
            "setuptools",
            "shellescape",
            "six",
            "typing",
            "testtools",
            "traceback2",
            "wheel",
            "x509",
            "zope.interface",]

setup(
    name=NAME,
    version=VERSION,
    description="SDK for the CyberSource REST API",
    author_email="developer@cybersource.com",
    url="",
    keywords=["Payments API", "CyberSource"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    CyberSource REST API
    """
)
