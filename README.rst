===============================
whichcraft
===============================

.. image:: https://badge.fury.io/py/whichcraft.png
    :target: http://badge.fury.io/py/whichcraft

.. image:: https://travis-ci.org/pydanny/whichcraft.png?branch=master
        :target: https://travis-ci.org/pydanny/whichcraft


This package provides cross-platform cross-python ``shutil.which`` functionality.

Usage
=====

On Linux, Mac, Windows for Python 2.6, 2.7, or any of the 3s:

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
