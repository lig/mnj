import pytest

from nj.document.document import Doc
from nj.document.exceptions import ClassAlreadyRegisteredError


def test_single_name_restriction(doc_registry):

    class C(Doc):
        meta = {
            'magic': True,
        }

    with pytest.raises(ClassAlreadyRegisteredError):
        class D(Doc):
            meta = {
                'magic': True,
                'class_name': 'C'
            }


def test_get_doc_class(doc_registry):

    class C(Doc):
        meta = {
            'magic': True,
        }

    class D(Doc):
        meta = {
            'magic': True,
        }

    assert doc_registry.get_class('C') is C
    assert doc_registry.get_class('D') is D
