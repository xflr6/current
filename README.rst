Current
=======

|PyPI version| |License| |Downloads|

Get the path of a file relative to the current module.
Import a Python module relative to the current module.
Temporarily change ``sys.path`` for imports.

Installation
------------

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


License
-------

`CC0 1.0 Public Domain Dedication
<https://creativecommons.org/publicdomain/zero/1.0/>`_


Changelog
---------

Version 0.1: First public release


.. |PyPI version| image:: https://pypip.in/v/current/badge.png
    :target: https://pypi.python.org/pypi/current
    :alt: Latest PyPI Version
.. |License| image:: https://pypip.in/license/current/badge.png
    :target: https://pypi.python.org/pypi/current
    :alt: License
.. |Downloads| image:: https://pypip.in/d/current/badge.png
    :target: https://pypi.python.org/pypi/current
    :alt: Downloads
