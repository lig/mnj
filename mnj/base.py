import collections


class BaseDoc(collections.OrderedDict):

    def __str__(self):
        return (
            '{' +
            ', '.join(['{}: {}'.format(k, v) for k, v in self.items()]) +
            '}')
