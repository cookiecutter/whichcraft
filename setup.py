#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.6.0"

if sys.argv[-1] == "publish":
    try:
        import wheel
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    try:
        import twine
    except ImportError:
        raise ImportError("Fix: pip install twine")        

    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You might want to tag a release now")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")


def get_requirements(filename):
    f = open(filename).read()
    reqs = [
        # loop through list of requirements
        x.strip()
        for x in f.splitlines()
        # filter out comments and empty lines
        if not x.strip().startswith("#")
    ]
    return reqs


setup(
    name="whichcraft",
    version=version,
    description="""This package provides cross-platform cross-python shutil.which functionality.""",
    long_description=readme + "\n\n" + history,
    author="Daniel Roy Greenfeld",
    author_email="pydanny@gmail.com",
    url="https://github.com/pydanny/whichcraft",
    include_package_data=True,
    py_modules=["whichcraft"],
    license="BSD",
    zip_safe=False,
    keywords="whichcraft",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
