from _weakref import proxy as _proxy
from collections import OrderedDict, _Link


class BaseDoc(OrderedDict):

    def __str__(self):
        return (
            '{' +
            ', '.join(['{}: {}'.format(k, v) for k, v in self.items()]) +
            '}')


class SortedDict(OrderedDict):

    def __setitem__(self, key, value,
                    dict_setitem=dict.__setitem__, proxy=_proxy, Link=_Link):
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
