Current
=======

|PyPI version| |License| |Downloads|

Get the path of a file relative to the current module. Import a Python module
relative to the current module. Temporarily change ``sys.path`` for imports.
Get the path of a file relative to the module of the current caller.


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
``inspect.currentframe``, see__ docs__). Under IronPython this might require
enabling the ``FullFrames`` option of the interpreter.

.. __: http://docs.python.org/2/library/sys.html#sys._getframe
.. __: http://docs.python.org/2/library/inspect.html#inspect.currentframe


License
-------

`CC0 1.0 Public Domain Dedication`__

.. __: http://creativecommons.org/publicdomain/zero/1.0/


Changelog
---------

Version 0.3: Added Python 3.3+ support.

Version 0.2.1: Fixed caller_path. Documented sys._getframe dependency.

Version 0.2: Added caller_path.

Version 0.1: First public release.


.. _pip: http://pip.readthedocs.org


.. |PyPI version| image:: https://pypip.in/v/current/badge.png
    :target: https://pypi.python.org/pypi/current
    :alt: Latest PyPI Version
.. |License| image:: https://pypip.in/license/current/badge.png
    :target: https://pypi.python.org/pypi/current
    :alt: License
.. |Downloads| image:: https://pypip.in/d/current/badge.png
    :target: https://pypi.python.org/pypi/current
    :alt: Downloads
