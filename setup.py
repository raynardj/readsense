from setuptools import setup
from setuptools import find_packages

setup(
    name="read_sense_book_store",
    version="0.1.0",
    author="raynardj",
    author_email="raynard@rasenn.com",
    description="An NLP based book store",
    packages = find_packages(),
    include_package_data=True,
    py_modules=['read_sense',],
    scripts = ['read_sense/bin/readrun',],
    package_data={'read_sense':['./app/templates/*','./app/translations/*']},
    install_requires = [
        # "flask==0.12.4",
        # "flask_appbuilder==1.10.0",
    ],
)