import attr
import bson
import pymongo

import mnj


def test_001_default_collection_name():
    class TestDocument(mnj.Document):
        pass

    assert TestDocument._meta.collection_name == "testDocument"


def test_002_explicit_collection_name():
    class TestDocument(mnj.Document):
        class Meta:
            collection_name = "my_document"

    assert TestDocument._meta.collection_name == "my_document"


def test_003_keep_collection_name_when_subclassing():
    class TestDocument(mnj.Document):
        class Meta:
            collection_name = "my_document"

    class TestDocumentChild(TestDocument):
        pass

    assert TestDocumentChild._meta.collection_name == "my_document"


def test_004_allow_to_override_collection_name_when_subclassing():
    class TestDocument(mnj.Document):
        class Meta:
            collection_name = "my_document"

    class TestDocumentChild(TestDocument):
        class Meta:
            collection_name = "my_child_document"

    assert TestDocumentChild._meta.collection_name == "my_child_document"


def test_005_document_col_property(mnj_client):
    class TestDocument(mnj.Document):
        pass

    assert isinstance(TestDocument._col, pymongo.collection.Collection)
    assert TestDocument._col.name == "testDocument"
    assert TestDocument._col.full_name == "test.testDocument"


def test_006_document_python_to_mongo(db, mnj_client, clean):
    class TestDocument(mnj.Document):
        str_attr: str
        int_attr: int
        float_attr: float

    TestDocument._col.insert_one(
        TestDocument(str_attr="test_value", int_attr=42, float_attr=6.2832)
    )

    actual_doc = db["testDocument"].find_one()

    assert isinstance(actual_doc["_id"], bson.ObjectId)

    del actual_doc["_id"]

    assert actual_doc == {
        "str_attr": "test_value",
        "int_attr": 42,
        "float_attr": 6.2832,
    }


def test_007_document_mongo_to_python(db, mnj_client, clean):
    class TestDocument(mnj.Document):
        str_attr: str
        int_attr: int
        float_attr: float

    db["testDocument"].insert_one(
        {"str_attr": "test_value", "int_attr": 42, "float_attr": 6.2832}
    )

    actual_doc = TestDocument._col.find_one()

    assert isinstance(actual_doc, TestDocument)

    actual_doc_data = attr.asdict(actual_doc)
    del actual_doc_data["_id"]

    assert actual_doc_data == {
        "str_attr": "test_value",
        "int_attr": 42,
        "float_attr": 6.2832,
    }
