# current.py - change sys.path for imports relative to the current module

__title__ = 'current'
__version__ = '0.2.1'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'CC0'

import os
import sys
import inspect
import contextlib

__all__ = ['current_path', 'inserted_path', 'caller_path']


def current_path(*names):
    """Return the path to names relative to the current module."""
    frame = inspect.currentframe()

    if __name__ != '__main__':
        frame = frame.f_back

    path = os.path.dirname(frame.f_code.co_filename)

    if names:
        path = os.path.join(path, *names)

    return os.path.realpath(path)


@contextlib.contextmanager
def inserted_path(directory=os.pardir, index=1):
    """Temporarily insert directory (os.pardir) to sys.path at index (1)"""
    frame = inspect.currentframe().f_back

    if __name__ != '__main__':
        frame = frame.f_back

    current_path = os.path.dirname(frame.f_code.co_filename)
    path = os.path.realpath(os.path.join(current_path, directory))

    oldpath = list(sys.path)
    sys.path.insert(index, path)

    try:
        yield
    finally:
        sys.path = oldpath


def caller_path(steps=1, names=None):
    """Return the path to the file of the current frames' caller."""
    frame = inspect.currentframe()

    for i in range(steps + 1):
        frame = frame.f_back

    path = os.path.dirname(frame.f_code.co_filename)

    if not path:
        path = os.getcwd()

    if names is not None:
        path = os.path.join(path, *names)

    return os.path.realpath(path)
