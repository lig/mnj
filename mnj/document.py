from collections import OrderedDict

from six import with_metaclass

from mnj.base import BaseDoc, SortedDict


__all__ = ['d']


class DocMeta(type):

    def __new__(cls, name, bases, attrs):

        # process meta
        meta = attrs.pop('meta', {})
        bases = list(bases)

        # is sorted
        if meta.get('sorted'):
            if OrderedDict in bases:
                bases[bases.index(OrderedDict)] = SortedDict
            else:
                bases.append(SortedDict)

        print(bases)
        return type.__new__(cls, name, tuple(bases), attrs)


class Doc(with_metaclass(DocMeta, BaseDoc)):
    pass


d = Doc
