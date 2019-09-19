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
    version="0.3.0",
    packages=find_packages(),
    install_requires=["pymongo"],
    tests_require=["pytest"],
    cmdclass={"test": PyTest},
    author="Serge Matveenko",
    author_email="s@matveenko.ru",
    url="https://github.com/lig/mnj",
    description=(
        "Mnj (Mongo Energy) is a helper library to simplify PyMongo" " interaction"
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: Database :: Front-Ends",
        "Typing :: Typed",
    ],
    license="BSD",
)
