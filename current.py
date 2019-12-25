# current.py - change sys.path for imports relative to the current module

import os
import sys
import contextlib

__all__ = ['current_path', 'inserted_path', 'caller_path']

__title__ = 'current'
__version__ = '0.3.6'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'CC0'


def current_path(*names):
    """Return the path to names relative to the current module."""
    depth = 0 if __name__ == '__main__' else 1

    frame = sys._getframe(depth)

    try:
        path = os.path.dirname(frame.f_code.co_filename)
    finally:
        del frame

    if names:
        path = os.path.join(path, *names)

    return os.path.realpath(path)


@contextlib.contextmanager
def inserted_path(directory=os.pardir, index=1):
    """Temporarily insert directory (os.pardir) to sys.path at index (1)."""
    depth = 1 if __name__ == '__main__' else 2

    frame = sys._getframe(depth)

    try:
        path = os.path.dirname(frame.f_code.co_filename)
    finally:
        del frame

    path = os.path.realpath(os.path.join(path, directory))

    oldpath = list(sys.path)
    sys.path.insert(index, path)

    try:
        yield
    finally:
        sys.path = oldpath


def caller_path(steps=1, names=None):
    """Return the path to the file of the current frames' caller."""
    frame = sys._getframe(steps + 1)

    try:
        path = os.path.dirname(frame.f_code.co_filename)
    finally:
        del frame

    if not path:
        path = os.getcwd()

    if names is not None:
        path = os.path.join(path, *names)

    return os.path.realpath(path)
