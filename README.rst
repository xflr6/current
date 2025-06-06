Current
=======

|PyPI version| |License| |Supported Python| |Downloads|

|Build| |Codecov|

Get the path of a file relative to the current module. Import a Python module
relative to the current module. Temporarily change ``sys.path`` for imports.
Get the path of a file relative to the module of the current caller.


Links
-----

- GitHub: https://github.com/xflr6/current
- PyPI: https://pypi.org/project/current/
- Issue Tracker: https://github.com/xflr6/current/issues
- Download: https://pypi.org/project/current/#files


Installation
------------

This package runs under Python 3.9+, use pip_ to install:

.. code:: bash

    $ pip install current


Usage
-----

Get paths relative to the current module:

.. code:: python

    >>> import current

    >>> here = current.current_path()
    >>> parent = current.current_path('..')
    >>> bruces = current.current_path('..', 'australia', 'bruces', 'bruces.ini')


Temporarily add the parent directory to ``sys.path``:

.. code:: python

    >>> with current.inserted_path()
    ...     import australia


Get paths relative to the module of the callers of the current code:

.. code:: python

    >>> caller = current.caller_path()
    >>> callercaller = current.caller_path(steps=2)


Potential issues
----------------

This package uses ``sys._getframe`` (which is almost the same as
``inspect.currentframe``, see_ docs_). Under IronPython this might require
enabling the ``FullFrames`` option of the interpreter.


License
-------

`CC0 1.0 Universal`_


Changelog
---------

Version 0.5 (in development): Drop Python 3.7 and 3.8 support; tag Python 3.11, 3.12, and 3.13 support. Switch to pyproject.toml.

Version 0.4.1: Drop Python 3.6 support.

Version 0.4: Drop Python 2 and 3.5 support; tag Python 3.9 and 3.10 support.

Version 0.3.6: Tag Python 3.8 support. Extend test coverage.

Version 0.3.5: Drop Python 3.4 support.

Version 0.3.4: Tag Python 3.7 support.

Version 0.3.3: Drop Python 3.3 support. Add python_requires.

Version 0.3.2: Port tests from nose/unittest to pytest. Update meta data, tag Python 3.5/3.6 support.

Version 0.3.1: Added wheel.

Version 0.3: Added Python 3.3+ support.

Version 0.2.1: Fixed caller_path. Documented sys._getframe dependency.

Version 0.2: Added caller_path.

Version 0.1: First public release.


.. _pip: https://pip.readthedocs.io

.. _see: https://docs.python.org/2/library/sys.html#sys._getframe
.. _docs: https://docs.python.org/2/library/inspect.html#inspect.currentframe

.. _CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/

.. |PyPI version| image:: https://img.shields.io/pypi/v/current.svg
    :target: https://pypi.org/project/current/
    :alt: Latest PyPI Version
.. |License| image:: https://img.shields.io/pypi/l/current.svg
    :target: https://github.com/xflr6/current/blob/master/LICENSE.txt
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/current.svg
    :target: https://pypi.org/project/current/
    :alt: Supported Python Versions
.. |Downloads| image:: https://img.shields.io/pypi/dm/current.svg
    :target: https://pypistats.org/packages/current
    :alt: Monthly downloads

.. |Build| image:: https://github.com/xflr6/current/actions/workflows/build.yaml/badge.svg?branch=master
    :target: https://github.com/xflr6/current/actions/workflows/build.yaml?query=branch%3Amaster
    :alt: Build
.. |Codecov| image:: https://codecov.io/gh/xflr6/current/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/xflr6/current
    :alt: Codecov
