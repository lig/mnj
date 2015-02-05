import pymongo


class MongoClient(pymongo.MongoClient):

    def __getattr__(self, name):
        """Get a database by name.

        See :class:`pymongo.mongo_client.MongoClient`.
        """
        return Database(self, name)


class Database(pymongo.database.Database):

    def __getattr__(self, name):
        """Get a collection of this database by name.

        See :class:`pymongo.database.Database`.
        """
        return Collection(self, name)


class Collection(pymongo.collection.Collection):

    def find(self, *args, **kwargs):
        """Query the database.

        See :class:`pymongo.collection.Collection`.
        """
        if 'slave_okay' not in kwargs:
            kwargs['slave_okay'] = self.slave_okay
        if 'read_preference' not in kwargs:
            kwargs['read_preference'] = self.read_preference
        if 'tag_sets' not in kwargs:
            kwargs['tag_sets'] = self.tag_sets
        if 'secondary_acceptable_latency_ms' not in kwargs:
            kwargs['secondary_acceptable_latency_ms'] = (
                self.secondary_acceptable_latency_ms)
        return Cursor(self, *args, **kwargs)


class Cursor(pymongo.cursor.Cursor):
    pass
