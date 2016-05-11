#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.4.0"

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

def get_requirements(filename):
    f = open(filename).read()
    reqs = [
            # loop through list of requirements
            x.strip() for x in f.splitlines()
                # filter out comments and empty lines
                if not x.strip().startswith('#')
            ]
    return reqs

setup(
    name='whichcraft',
    version=version,
    description="""This package provides cross-platform cross-python shutil.which functionality.""",
    long_description=readme + '\n\n' + history,
    author='Daniel Roy Greenfeld',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/whichcraft',
    include_package_data=True,
    py_modules=['whichcraft'],
    license="BSD",
    zip_safe=False,
    keywords='whichcraft',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
