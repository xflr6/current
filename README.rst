Current
=======

|PyPI version| |License| |Supported Python| |Format| |Downloads|

Get the path of a file relative to the current module. Import a Python module
relative to the current module. Temporarily change ``sys.path`` for imports.
Get the path of a file relative to the module of the current caller.


Links
-----

- GitHub: http://github.com/xflr6/current
- PyPI: http://pypi.python.org/pypi/current
- Issue Tracker: http://github.com/xflr6/current/issues
- Download: http://pypi.python.org/pypi/current#downloads


Installation
------------

This package runs under Python 2.7 and 3.3+, use pip_ to install:

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

`CC0 1.0 Public Domain Dedication`_


Changelog
---------

Version 0.3.2 (in development): 

Version 0.3.1: Added wheel.

Version 0.3: Added Python 3.3+ support.

Version 0.2.1: Fixed caller_path. Documented sys._getframe dependency.

Version 0.2: Added caller_path.

Version 0.1: First public release.


.. _pip: http://pip.readthedocs.io

.. _see: http://docs.python.org/2/library/sys.html#sys._getframe
.. _docs: http://docs.python.org/2/library/inspect.html#inspect.currentframe

.. _CC0 1.0 Public Domain Dedication: http://creativecommons.org/publicdomain/zero/1.0/

.. |PyPI version| image:: https://img.shields.io/pypi/v/current.svg
    :target: https://pypi.python.org/pypi/current
    :alt: Latest PyPI Version
.. |License| image:: https://img.shields.io/pypi/l/current.svg
    :target: https://pypi.python.org/pypi/current
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/current.svg
    :target: https://pypi.python.org/pypi/current
    :alt: Supported Python Versions
.. |Format| image:: https://img.shields.io/pypi/format/current.svg
    :target: https://pypi.python.org/pypi/current
    :alt: Format
.. |Downloads| image:: https://img.shields.io/pypi/dm/current.svg
    :target: https://pypi.python.org/pypi/current
    :alt: Downloads
