__all__ = ['gt_', 'gte_', 'in_', 'lt_', 'lte_', 'ne_', 'nin_']


def gt_(value):
    return {'$gt': value}


def gte_(value):
    return {'$gte': value}


def in_(*values):
    return {'$in': values}


def lt_(value):
    return {'$lt': value}


def lte_(value):
    return {'$lte': value}


def ne_(value):
    return {'$ne': value}


def nin_(*values):
    return {'$nin': values}
