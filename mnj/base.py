from collections import OrderedDict


class BaseDoc(OrderedDict):

    def __str__(self):
        return (
            '{' +
            ', '.join(['{}: {}'.format(k, v) for k, v in self.items()]) +
            '}')
