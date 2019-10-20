import bson.json_util


class MongoObject(dict):
    def __str__(self) -> str:
        return bson.json_util.dumps(self)
