import os
from codecs import open
from os import path

from setuptools import setup, find_packages, Command

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ytils',
    version='v0.0.1',

    description='ytils',
    long_description=long_description,
    url='https://github.com/yiwc/ytils',

    license='MIT',

    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],

    keywords=[""],

    packages=find_packages(exclude=[]),

    install_requires=[
        "pandas",
        "numpy"
    ]


)