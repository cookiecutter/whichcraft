===============================
whichcraft
===============================

.. image:: https://badge.fury.io/py/whichcraft.svg
    :target: http://badge.fury.io/py/whichcraft

.. image:: https://travis-ci.org/pydanny/whichcraft.svg?branch=master
        :target: https://travis-ci.org/pydanny/whichcraft

.. image:: https://codecov.io/gh/pydanny/whichcraft/branch/master/graph/badge.svg
        :target: http://codecov.io/github/pydanny/whichcraft?branch=master

.. image:: https://ci.appveyor.com/api/projects/status/v9coijayykhkeu4d?svg=true
        :target: https://ci.appveyor.com/project/pydanny/whichcraft

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

::

    That code in my care
    That sly command-line stare
    That strips my operating system bare
    It's whichcraft

This package provides cross-platform cross-python ``shutil.which`` functionality.

Usage
=====

On Linux, Mac, Windows for Python 2.7 or any of the maintained 3s:

.. code-block:: python

    >>> from whichcraft import which
    >>> which('date')
    '/bin/date'
    >>> which('calendar')
    '/bin/calendar'
    >>> which('cookiecutter')
    '/Users/pydanny/.envs/fun/bin/cookiecutter'
    >>> which('a-made-up-name') is None
    True


Notes
=====

This is a shim of the ``shutil.which`` function that's designed to work across
multiple versions of Python and inside of windows. The code for Python 2.x is
based on Python 3 code that I extracted from source. I originally did this for
Cookiecutter_ but pulled it out in order to reduce line count for that project.

Edgecase: Date function works perfectly on mac os and linux system, hence returns string.
But is an in-built function in windows hence returns none as value when called in
windows.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
