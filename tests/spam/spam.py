# spam.py

import current


def current_path():
    return current.current_path()

def caller_path():
    return current.caller_path()

def eggs():
    from .eggs.eggs import caller_path
    return caller_path()
