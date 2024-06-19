# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "cybersource-rest-client-python"
VERSION = "0.0.55"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="SDK for the CyberSource REST API",
    author_email="developer@cybersource.com",
    url="https://github.com/CyberSource/cybersource-rest-client-python",
    keywords=["Payments API", "CyberSource"],
    install_requires=[
        "certifi",
        "pycryptodome",
        "PyJWT",
        "pyOpenSSL<=23.2.0",
        "DateTime",
        "setuptools",
        "six",
        "urllib3",
        "jwcrypto==1.5.1;python_version<='3.7'",
        "jwcrypto>=1.5.6;python_version>'3.7'",
        "cryptography==40.0.2;python_version<='3.6'",
        "cryptography<41.1.0;python_version>'3.6'"
    ],
    packages=find_packages(),
    include_package_data=True,
    long_description="CyberSource REST API",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
