from __future__ import print_function

from collections import OrderedDict

from six import with_metaclass

from mnj.base import BaseDoc, SortedDict
from mnj.compat import ChainMap
from mnj.doc_registry import doc_registry


__all__ = ['d']


class DocMeta(type):

    meta_defaults = {
        'sorted': False,
        'magic': False,
        'class_name': None,  # actual class name is used by default
    }

    def __new__(cls, name, bases, attrs):

        # process meta
        meta = ChainMap(
            attrs.pop('meta', {}),
            {'class_name': name},
            cls.meta_defaults,
        )

        # prepare bases for modification
        bases = list(bases)

        # is sorted
        if meta['sorted']:
            if OrderedDict in bases:
                bases[bases.index(OrderedDict)] = SortedDict
            else:
                bases.append(SortedDict)

        # is magic (keep this section last)
        if meta['magic']:
            if Doc in bases:
                bases.insert(bases.index(Doc), MagicMixin)
            else:
                bases.append(MagicMixin)
            attrs['_cls'] = meta['class_name']
            type_new = type.__new__(cls, name, tuple(bases), attrs)
            doc_registry.register_class(type_new)
            return type_new
        else:
            return type.__new__(cls, name, tuple(bases), attrs)


class MagicMixin(object):

    _cls = None

    def __init__(self, *args, **kwargs):
        return super(MagicMixin, self).__init__(*args, **kwargs)


class Doc(with_metaclass(DocMeta, BaseDoc)):
    pass


d = Doc
