from pymongo import MongoClient

from mnj import *


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
