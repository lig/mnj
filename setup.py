import sys

from setuptools import setup, find_packages
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


install_requires = [
    'six',
    'pymongo',
]
if sys.version_info.major < 3:
    install_requires += [
        'chainmap',
    ]
if sys.version_info[:2] < (3, 4):
    install_requires += [
        'enum34',
    ]

setup(
    name='mnj',
    version='0.2dev1',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=[
        'pytest',
    ],
    cmdclass={'test': PyTest},
    author='Serge Matveenko',
    author_email='s@matveenko.ru',
    description=(
        'Mnj (Mongo Energy) is a helper library to simplify PyMongo'
        ' interaction'),
    url='https://github.com/lig/mnj',
    license='BSD',
)
