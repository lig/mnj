import pytest

from mnj.document import Doc
from mnj.exceptions import DocAlreadyRegisteredError


def test_single_name_restriction():

    class C(Doc):
        meta = {
            'magic': True,
        }

    with pytest.raises(DocAlreadyRegisteredError):
        class D(Doc):
            meta = {
                'magic': True,
                'class_name': 'C'
            }
