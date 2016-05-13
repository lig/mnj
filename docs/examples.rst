Examples
========

Basic Usage
-----------

::

    from mnj import *
    from pymongo import MongoClient


    db = MongoClient()['test']
    db.docs.drop()
    db.docs.insert_one(d([('a', 1), ('b', 1)]))
    db.docs.insert_one(d([('a', 2), ('b', 2)]))
    db.docs.insert_one(d([('a', 3), ('b', 3)]))
    db.docs.insert_one(d([('a', 1), ('b', 4)]))
    db.docs.insert_one(d([('a', 2), ('b', 5)]))
    db.docs.insert_one(d([('a', 3), ('b', 6)]))

    # {'a': 1, 'b': 1}
    # {'a': 1, 'b': 4}
    for doc in db.docs.find(q(a=1)):
        print(doc)

    # {'a': 1, 'b': 1}
    # {'a': 3, 'b': 3}
    # {'a': 1, 'b': 4}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(a=ne_(2))):
        print(doc)

    # {'a': 1, 'b': 4}
    # {'a': 2, 'b': 5}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(b=gt_(3))):
        print(doc)

    # {'a': 2, 'b': 2}
    # {'a': 3, 'b': 3}
    # {'a': 3, 'b': 6}
    for doc in db.docs.find(q(a=3) | q(b=2)):
        print(doc)

    # {'a': 1, 'b': 4}
    for doc in db.docs.find(and_(q(a=1), q(b=4))):
        print(doc)
