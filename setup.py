from setuptools import setup, find_packages


setup(
    name='mnj',
    version='0.1dev',
    packages=find_packages(),
    install_requires=[
        'pymongo',
    ],
    tests_require=[
        'pytest',
    ],
    author='Serge Matveenko',
    author_email='s@matveenko.ru',
    description=(
        'Mnj (Mongo Energy) is a helper library to simplify PyMongo'
        ' interaction'),
    license='BSD',
)
