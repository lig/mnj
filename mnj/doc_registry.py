from mnj.exceptions import DocAlreadyRegisteredError


__all__ = ['doc_registry']


class DocRegistry(object):
    _registry = {}

    def register_doc(self, doc_class):
        name = doc_class._cls

        if name in self._registry:
            raise DocAlreadyRegisteredError(
                'Class %s is already registered', name)

        self._registry[name] = doc_class

doc_registry = DocRegistry()
