#-*-coding:utf-8-*-

import os
from setuptools import setup

def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath, 'r') as fp:
        return fp.read()

setup(
    name='memobird',
    version='0.1.1',
    description='Memobird Python SDK',
    long_description=fread('README.md'),
    keywords='memobird',
    url='https://github.com/wong2/memobird.py',
    author='wong2',
    author_email='wonderfuly@gmail.com',
    license='MIT',
    py_modules=['memobird'],
    install_requires=[
        'Pillow==9.0.0',
        'requests==2.9.1',
    ],
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
