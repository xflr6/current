# current.py - change sys.path for imports relative to the current module

import os
import sys
import inspect
import contextlib

__all__ = ['current_path', 'inserted_path']


def current_path(*names):
    frame = inspect.currentframe()

    if __name__ != '__main__':
        frame = frame.f_back

    result = os.path.dirname(frame.f_code.co_filename)

    if names:
        result = os.path.join(result, *names)

    return os.path.realpath(result)


@contextlib.contextmanager
def inserted_path(name=os.pardir, index=1):
    frame = inspect.currentframe().f_back

    if __name__ != '__main__':
        frame = frame.f_back

    current_path = os.path.dirname(frame.f_code.co_filename)
    path = os.path.realpath(os.path.join(current_path, name))

    oldpath = list(sys.path)
    sys.path.insert(index, path)

    try:
        yield
    finally:
        sys.path = oldpath
