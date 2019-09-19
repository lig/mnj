import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    # user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name="mnj",
    version="0.2.1",
    packages=find_packages(),
    install_requires=["pymongo"],
    tests_require=["pytest"],
    cmdclass={"test": PyTest},
    author="Serge Matveenko",
    author_email="s@matveenko.ru",
    description=(
        "Mnj (Mongo Energy) is a helper library to simplify PyMongo" " interaction"
    ),
    url="https://github.com/lig/mnj",
    license="BSD",
)
