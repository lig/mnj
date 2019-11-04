import re


try:
    Pattern = re.Pattern  # type: ignore
except AttributeError:
    # Python <3.7
    Pattern = re._pattern_type  # type: ignore
