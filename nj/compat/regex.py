import re


try:
    Pattern = re.Pattern
except AttributeError:
    # Python <3.7
    Pattern = re._pattern_type
