from fizzbuzz_utils.fizzbuzz import is_fizzbuzz
import unittest

class TestCasesfizz(unittest.TestCase):
    def test_fizz(self):
        x = 3
        fizzbuzz = is_fizzbuzz(x)
        self.assertEqual(fizzbuzz, "fizz")
    def test_buzz(self):
        x = 10
        fizzbuzz = is_fizzbuzz(x)
        self.assertEqual(fizzbuzz, "buzz")
    def test_fizzbuzz(self):
        x = 15
        fizzbuzz = is_fizzbuzz(x)
        self.assertEqual(fizzbuzz, "fizzbuzz")
