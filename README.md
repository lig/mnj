[![Join the chat at https://gitter.im/lig/mnj](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/lig/mnj?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/lig/mnj.svg?branch=develop)](https://travis-ci.org/lig/mnj)
[![Coverage Status](https://coveralls.io/repos/github/lig/mnj/badge.svg?branch=develop)](https://coveralls.io/github/lig/mnj?branch=develop)

# Mnj

![Mnj Logo](https://www.dropbox.com/s/492ke98ciajnd98/logo150.png?dl=1)

**Mnj** (_Mongo Energy_) is a helper library to simplify PyMongo interaction

## Install
Untill Mnj release will be available via PyPI you may get somewhat ready to use snapshot via

    pip install --pre mnj

or clone this repository to get the latest source and invoke install

    python setup.py install

## Features
* Using `mnj.q` object for constructing queries will help to validate them.
* No creepy `'$op'` strings any more use `op_()` style operators.

## Usage
Basic usage. Try yourself via `python -m mnj`.
```python
    from mnj import *
    from pymongo import MongoClient


    db = MongoClient(document_class=d)['test']
    db.docs.drop()
    db.docs.insert(d([('a', 1), ('b', 1)]))
    db.docs.insert(d([('a', 2), ('b', 2)]))
    db.docs.insert(d([('a', 3), ('b', 3)]))
    db.docs.insert(d([('a', 1), ('b', 4)]))
    db.docs.insert(d([('a', 2), ('b', 5)]))
    db.docs.insert(d([('a', 3), ('b', 6)]))

    # {'a': 1, 'b': 1}
    # {'a': 1, 'b': 4}
    for doc in db.docs.find(q(a=1)):
        del doc['_id']
        print(doc)
    print()

    # {'a': 1, 'b': 1}
    # {'a': 3, 'b': 3}
    # {'a': 1, 'b': 4}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(a=ne_(2))):
        del doc['_id']
        print(doc)
    print()

    # {'a': 1, 'b': 4}
    # {'a': 2, 'b': 5}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(b=gt_(3))):
        del doc['_id']
        print(doc)
    print()

    # {'a': 2, 'b': 2}
    # {'a': 3, 'b': 3}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(a=3) | q(b=2)):
        del doc['_id']
        print(doc)
    print()

    # {'a': 1, 'b': 4}
    for doc in db.docs.find(and_(q(a=1), q(b=4))):
        del doc['_id']
        print(doc)
    print()
```
