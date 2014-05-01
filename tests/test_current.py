# test_current.py

import unittest

import os

import current

import spam.spam
import spam.eggs.eggs


class TestCurrentPath(unittest.TestCase):

    def test_from_test(self):
        self.assertEqual(os.path.split(current.current_path())[-1], 'tests')

    def test_from_spam(self):
        self.assertEqual(os.path.split(spam.spam.current_path())[-1], 'spam')

    def test_from_eggs(self):
        self.assertEqual(os.path.split(spam.eggs.eggs.current_path())[-1], 'eggs')


class TestCallerPath(unittest.TestCase):

    def test_from_test(self):
        self.assertEqual(os.path.split(spam.spam.caller_path())[-1], 'tests')
        self.assertEqual(os.path.split(spam.eggs.eggs.caller_path())[-1], 'tests')

    def test_from_spam(self):
        self.assertEqual(os.path.split(spam.spam.eggs())[-1], 'spam')

    def test_from_eggs(self):
        self.assertEqual(os.path.split(spam.eggs.eggs.spam())[-1], 'eggs')
