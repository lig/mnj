import collections

import six


@six.python_2_unicode_compatible
class BaseDoc(collections.OrderedDict):

    def __str__(self):
        return (
            '{' +
            ', '.join(
                ['{}: {}'.format(k, v) for k, v in six.iteritems(self)]
            ) +
            '}')
