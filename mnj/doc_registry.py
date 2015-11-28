from mnj.exceptions import ClassAlreadyRegisteredError, ClassIsNotRegistered


__all__ = ['doc_registry']


class DocRegistry(object):
    _registry = {}

    def register_class(self, doc_class):
        class_name = doc_class._cls

        if class_name in self._registry:
            raise ClassAlreadyRegisteredError(
                'Class %s is already registered', class_name)

        self._registry[class_name] = doc_class

    def get_class(self, class_name):

        if class_name not in self._registry:
            raise ClassIsNotRegistered(
                'Class %s is not registered', class_name)

        return self._registry[class_name]

doc_registry = DocRegistry()
