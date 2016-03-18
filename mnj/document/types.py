import enum


@enum.unique
class BSONType(enum.Enum):
    Double = 1
    String = 2
    Object = 3
    Array = 4
    BinaryData = 5
    Undefined = 6
    ObjectId = 7
    Boolean = 8
    Date = 9
    Null = 10
    RegularExpression = 11
    JavaScript = 13
    Symbol = 14
    JavaScriptWithScope = 15
    Integer32Bit = 16
    Timestamp = 17
    Integer64Bit = 18
    MinKey = -1
    MaxKey = 127

BSON_DOUBLE = BSONType['Double']
BSON_STRING = BSONType['String']
BSON_OBJECT = BSONType['Object']
BSON_ARRAY = BSONType['Array']
BSON_BINARY_DATA = BSONType['BinaryData']
BSON_UNDEFINED = BSONType['Undefined']
BSON_OBJECT_ID = BSONType['ObjectId']
BSON_BOOLEAN = BSONType['Boolean']
BSON_DATE = BSONType['Date']
BSON_NULL = BSONType['Null']
BSON_REGULAR_EXPRESSION = BSONType['RegularExpression']
BSON_JAVASCRIPT = BSONType['JavaScript']
BSON_SYMBOL = BSONType['Symbol']
BSON_JAVASCRIPT_WITH_SCOPE = BSONType['JavaScriptWithScope']
BSON_32BIT_INTEGER = BSONType['Integer32Bit']
BSON_TIMESTAMP = BSONType['Timestamp']
BSON_64BIT_INTEGER = BSONType['Integer64Bit']
BSON_MIN_KEY = BSONType['MinKey']
BSON_MAX_KEY = BSONType['MaxKey']
