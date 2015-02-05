from .query import q

__all__ = ['or_']


def or_(first, second):
    return q({'$or': [q(first), q(second)]})
