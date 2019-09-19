import collections

from mnj.document.base import BaseDoc
from mnj.document.registry import registry


__all__ = ['d']


class DocMeta(type):

    meta_defaults = {
        'magic': False,
        'class_name': None,  # actual class name is used by default
    }

    def __new__(cls, name, bases, attrs):

        # process meta
        meta = collections.ChainMap(
            attrs.pop('meta', {}), {'class_name': name}, cls.meta_defaults
        )

        # prepare bases for modification
        bases = list(bases)

        # is magic (keep this section last)
        if meta['magic']:
            if Doc in bases:
                bases.insert(bases.index(Doc), MagicMixin)
            else:
                bases.append(MagicMixin)
            attrs['_cls'] = meta['class_name']
            type_new = type.__new__(cls, name, tuple(bases), attrs)
            registry.register_class(type_new)
            return type_new
        else:
            return type.__new__(cls, name, tuple(bases), attrs)


class MagicMixin(object):

    _cls = None

    def __init__(self, *args, **kwargs):
        return super(MagicMixin, self).__init__(*args, **kwargs)


class Doc(BaseDoc, metaclass=DocMeta):
    pass


d = Doc
