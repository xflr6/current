# test_current.py

import sys

if sys.version_info.major == 2:
    import pathlib2 as pathlib
    ModuleNotFoundError = ImportError
else:
    import pathlib

import pytest

import current

import spam.spam
import spam.eggs.eggs


@pytest.mark.parametrize('module, names, expected_end', [
    (current, [], ('tests',)),
    (current, ['spam.txt'], ('tests', 'spam.txt')),
    (current, ['spam', 'eggs'], ('tests', 'spam', 'eggs')),
    (spam.spam, [], ('tests', 'spam')),
    (spam.eggs.eggs, [], ('tests', 'spam', 'eggs')),
])
def test_current_path(module, names, expected_end):
    func = getattr(module, 'current_path')
    result = func(*names)
    path = pathlib.Path(result)
    assert path.parts[-len(expected_end):] == expected_end


def test_inserted_path(tmpdir):
    modpath = tmpdir / 'module.py'
    modpath.write_text(u'answer = lambda: 42', encoding='ascii', ensure=True)
    with (tmpdir / 'subdir').mkdir().as_cwd():
        with pytest.raises(ModuleNotFoundError, match=r'No module named'):
            import module
        with current.inserted_path(str(modpath.dirname)):
            import module
            assert module.answer() == 42
        del sys.modules['module']
        with pytest.raises(ModuleNotFoundError, match=r'No module named'):
            import module


@pytest.mark.parametrize('func, names, expected_end', [
    (current.caller_path, ['spam'], ('spam',)),
    (spam.spam.caller_path, None, ('tests',)),
    (spam.eggs.eggs.caller_path, None, ('tests',)),
    (eval('lambda: (lambda: current.caller_path())()'), None, ('current',)),
    (spam.spam.eggs, None, ('tests', 'spam')),
    (spam.eggs.eggs.spam, None, ('tests', 'spam', 'eggs')),
])
def test_caller_path(func, names, expected_end):
    kwargs = {'names': names} if names is not None else {}
    result = func(**kwargs)
    path = pathlib.Path(result)
    assert path.parts[-len(expected_end):] == expected_end
