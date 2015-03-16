# Mnj
![Mnj Logo](https://www.dropbox.com/s/492ke98ciajnd98/logo150.png?dl=1)

**Mnj** (_Mongo Energy_) is a helper library to simplify PyMongo interaction

## Install
Untill Mnj release will be available via PyPI clone this repository and invoke install

    python setup.py install

## Features
* Using `mnj.MongoClient` will set `OrderedDict` instead of `dict` as document class by default.
* Using `mnj.q` object for constructing queries will help to validate them.
* No creepy `'$op'` strings any more use `_op()` from `mnj.operators`.

## Planned
* More precise query validation including query structure and data types.
* Schema validation

## Usage
Basic usage

    from mnj.base import MongoClient
    from mnj.operators import *
    from mnj.query import q, Doc
    
    
    db = MongoClient()['test']
    db.docs.drop()
    db.docs.insert(Doc([('a', 1), ('b', 1)]))
    db.docs.insert(Doc([('a', 2), ('b', 2)]))
    db.docs.insert(Doc([('a', 3), ('b', 3)]))
    db.docs.insert(Doc([('a', 1), ('b', 4)]))
    db.docs.insert(Doc([('a', 2), ('b', 5)]))
    db.docs.insert(Doc([('a', 3), ('b', 6)]))
    
    # {'a': 1, 'b': 1}
    # {'a': 1, 'b': 4}
    db.docs.find(q(a=1))
    
    # {'a': 1, 'b': 1}
    # {'a': 3, 'b': 3}
    # {'a': 1, 'b': 4}
    # {'a': 3, 'b': 6}
    db.docs.find(q(a=_ne(2)))

    # {'a': 1, 'b': 4}
    # {'a': 2, 'b': 5}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(b=_gt(3)))

    # {'a': 2, 'b': 2}
    # {'a': 3, 'b': 3}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(a=3) | q(b=2))

    # {'a': 1, 'b': 4}
    for doc in db.docs.find(_and(q(a=1), q(b=4)))
