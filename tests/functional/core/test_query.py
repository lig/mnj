import nj
import nj.core.query


def test_001_query_method_return_query_instance():
    class TestDocument(nj.Document):
        pass

    query = TestDocument.query()

    assert isinstance(query, nj.core.query.Query)


def test_002_query_document_class_property(db):
    class TestDocument(nj.Document):
        pass

    query = TestDocument.query()

    assert query._document_class is TestDocument
