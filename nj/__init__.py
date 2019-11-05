from nj.core.base import MongoObject
from nj.core.client import create_client, get_client, get_db
from nj.core.document import Document
from nj.core.query import Q as q
from nj.core.registry import DocumentFactory
from nj.core.types import (
    BSON_32BIT_INTEGER,
    BSON_64BIT_INTEGER,
    BSON_ARRAY,
    BSON_BINARY_DATA,
    BSON_BOOLEAN,
    BSON_DATE,
    BSON_DOUBLE,
    BSON_JAVASCRIPT,
    BSON_JAVASCRIPT_WITH_SCOPE,
    BSON_MAX_KEY,
    BSON_MIN_KEY,
    BSON_NULL,
    BSON_OBJECT,
    BSON_OBJECT_ID,
    BSON_REGULAR_EXPRESSION,
    BSON_STRING,
    BSON_SYMBOL,
    BSON_TIMESTAMP,
    BSON_UNDEFINED,
    BSONType,
)
from nj.operators.query.array import all_, elem_match_, size_
from nj.operators.query.bitwise import (
    bits_all_clear_,
    bits_all_set_,
    bits_any_clear_,
    bits_any_set_,
)
from nj.operators.query.comparison import gt_, gte_, in_, lt_, lte_, ne_, nin_
from nj.operators.query.element import exists_, type_
from nj.operators.query.evaluation import mod_, regex_, text_, where_
from nj.operators.query.logical import and_, nor_, not_, or_


__all__ = [
    'all_',
    'and_',
    'bits_all_clear_',
    'bits_all_set_',
    'bits_any_clear_',
    'bits_any_set_',
    'BSON_32BIT_INTEGER',
    'BSON_64BIT_INTEGER',
    'BSON_ARRAY',
    'BSON_BINARY_DATA',
    'BSON_BOOLEAN',
    'BSON_DATE',
    'BSON_DOUBLE',
    'BSON_JAVASCRIPT_WITH_SCOPE',
    'BSON_JAVASCRIPT',
    'BSON_MAX_KEY',
    'BSON_MIN_KEY',
    'BSON_NULL',
    'BSON_OBJECT_ID',
    'BSON_OBJECT',
    'BSON_REGULAR_EXPRESSION',
    'BSON_STRING',
    'BSON_SYMBOL',
    'BSON_TIMESTAMP',
    'BSON_UNDEFINED',
    'BSONType',
    'create_client',
    'Document',
    'DocumentFactory',
    'elem_match_',
    'exists_',
    'get_client',
    'get_db',
    'gt_',
    'gte_',
    'in_',
    'lt_',
    'lte_',
    'mod_',
    'MongoObject',
    'ne_',
    'nin_',
    'nor_',
    'not_',
    'or_',
    'q',
    'regex_',
    'size_',
    'text_',
    'type_',
    'where_',
]
