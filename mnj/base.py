from _weakref import proxy as _proxy

import six

from mnj.compat import OrderedDict

if six.PY3:
    from collections import _Link
else:
    _Link = None


class BaseDoc(OrderedDict):

    def __str__(self):
        return (
            '{' +
            ', '.join(['{}: {}'.format(k, v) for k, v in self.items()]) +
            '}')


class SortedDict(OrderedDict):

    def __setitem3__(
            self, key, value, dict_setitem=dict.__setitem__, proxy=_proxy,
            Link=_Link):
        'sd.__setitem__(i, y) <==> sd[i]=y'
        # Setting a new item creates a new link before first item greater than
        # the one being inserted,
        # and the inherited dictionary is updated with the new key/value pair.
        if key not in self:
            _root = self._OrderedDict__root
            _map = self._OrderedDict__map
            place = _root
            for k in sorted(self.keys()):
                if k > key:
                    place = _map[k]
                    break
            _map[key] = link = Link()
            last = place.prev
            link.prev, link.next, link.key = last, place, key
            last.next = link
            place.prev = proxy(link)
        dict_setitem(self, key, value)

    def __setitem2__(self, key, value, dict_setitem=dict.__setitem__):
        'od.__setitem__(i, y) <==> od[i]=y'
        # Setting a new item creates a new link at the end of the linked list,
        # and the inherited dictionary is updated with the new key/value pair.
        if key not in self:
            _root = self._OrderedDict__root
            _map = self._OrderedDict__map
            place = _root
            for k in sorted(self.keys()):
                if k > key:
                    place = _map[k]
                    break
            last = place[0]
            last[1] = place[0] = _map[key] = [last, place, key]
        return dict_setitem(self, key, value)

    __setitem__ = six.PY3 and __setitem3__ or __setitem2__
