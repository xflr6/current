# eggs.py

import current


def current_path():
    return current.current_path()

def caller_path():
    return current.caller_path()

def spam():
    from spam.spam import caller_path
    return caller_path()
