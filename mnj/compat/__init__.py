import sys

if sys.version_info < (3, 5):
    from collections import OrderedDict
else:
    from mnj.compat.ordereddict35 import OrderedDict
