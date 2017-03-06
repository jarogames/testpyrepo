import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


#https://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(
    name = "testpyrepo",
    version = "0.0.1",
    author = "Carodej",
    author_email = "carodej@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "GPLv2",
    keywords = "example  tutorial",
    url = "http://www.seznam.cz",
    packages=['NuPyPhy', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)
