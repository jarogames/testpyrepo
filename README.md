# testpyrepo
test to build python repo

The aim is to create an installable package - **MySuperPackage**

# creation

Use git versioning system, upload to github. The file structure is:

*  README.md  requirements.txt  setup.py  ... they contain stuff, requirements.txt: pip freeze

* MySuperPackage/__init__.py

# Versioning

 * git tag v0.0.1 ... lightweight tag

 * put it into setup.py


# Installation

* `python setup.py install` ... it creates egg - not very much clear to me

* `pip install git+git://github.com/jarogames/testpyrepo@master` ... this is great - it creates MySuperPackage that can be imported in */home/ojr/anaconda3/lib/python3.5/site-packages/MySuperPackage*


