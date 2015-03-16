from mnj.base import MongoClient
from mnj.operators.comparison import _gt, _ne
from mnj.operators.logical import _and
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
for doc in db.docs.find(q(a=1)):
    del doc['_id']
    print(doc)
print()

# {'a': 1, 'b': 1}
# {'a': 3, 'b': 3}
# {'a': 1, 'b': 4}
# {'a': 3, 'b': 6}
for doc in db.docs.find(q(a=_ne(2))):
    del doc['_id']
    print(doc)
print()

# {'a': 1, 'b': 4}
# {'a': 2, 'b': 5}
# {'a': 3, 'b': 6}
for doc in db.docs.find(q(b=_gt(3))):
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
for doc in db.docs.find(_and(q(a=1), q(b=4))):
    del doc['_id']
    print(doc)
print()
