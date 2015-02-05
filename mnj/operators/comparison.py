__all__ = ['_gt', '_gte', '_in', '_lt', '_lte', '_ne', '_nin']


def _gt(value):
    return {'$gt': value}


def _gte(value):
    return {'$gte': value}


def _in(*values):
    return {'$in': values}


def _lt(value):
    return {'$lt': value}


def _lte(value):
    return {'$lte': value}


def _ne(value):
    return {'$ne': value}


def _nin(*values):
    return {'$nin': values}
