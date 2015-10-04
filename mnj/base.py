from collections import OrderedDict


__all__ = []


class Doc(OrderedDict):

    def __str__(self):
        return (
            '{' +
            ', '.join(['{}: {}'.format(k, v) for k, v in self.items()]) +
            '}')
