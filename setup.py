import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
##############
#packages=[]   #  directory with __init__.py
#modules=[]    #  single files in root dir
#https://pythonhosted.org/an_example_pypi_project/setuptools.html
#
#https://pypi.python.org/pypi?%3Aaction=list_classifiers
#
setup(
    name = "testpyrepo",
    version = "0.0.1",
    zip_safe= False,
    author = "Carodej",
    author_email = "carodej@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "GPLv2",
    keywords = "example  tutorial",
    url = "http://www.seznam.cz",
    packages=['MySuperPackage'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)
