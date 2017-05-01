# test_current.py

import os

import current

import spam.spam
import spam.eggs.eggs


def test_current_from_test():
    assert os.path.split(current.current_path())[-1] == 'tests'


def test_current_from_spam():
    assert os.path.split(spam.spam.current_path())[-1] == 'spam'


def test_current_from_eggs():
    assert os.path.split(spam.eggs.eggs.current_path())[-1] == 'eggs'


def test_caller_path_from_test():
    assert os.path.split(spam.spam.caller_path())[-1] == 'tests'
    assert os.path.split(spam.eggs.eggs.caller_path())[-1] == 'tests'


def test_caller_path_from_spam():
    assert os.path.split(spam.spam.eggs())[-1] == 'spam'


def test_caller_path_from_eggs():
    assert os.path.split(spam.eggs.eggs.spam())[-1] == 'eggs'
