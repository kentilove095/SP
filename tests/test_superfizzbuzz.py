from superfizzbuzz_utils.superfizzbuzz import superfizzbuzz
import unittest


class TestCaseMod3(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 3
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "Fizz", "Fizz")

    def test_give_middle_number(self):
        num = 5001
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "Fizz", "Fizz")

    def test_give_highest_number(self):
        num = 9996
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "Fizz", "Fizz")


class TestCaseMod5(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 5
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "Buzz", "Buzz")

    def test_give_middle_number(self):
        num = 5005
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "Buzz", "Buzz")

    def test_give_highest_number(self):
        num = 9995
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "Buzz", "Buzz")


class TestCaseMod3And5(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 15
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzBuzz", "FizzBuzz")

    def test_give_middle_number(self):
        num = 4980
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzBuzz", "FizzBuzz")

    def test_give_highest_number(self):
        num = 9975
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzBuzz", "FizzBuzz")


class TestCaseMod9(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 9
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzFizz", "FizzFizz")

    def test_give_middle_number(self):
        num = 4986
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzFizz", "FizzFizz")

    def test_give_highest_number(self):
        num = 9999
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzFizz", "FizzFizz")


class TestCaseMod25(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 25
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "BuzzBuzz", "BuzzBuzz")

    def test_give_middle_number(self):
        num = 5000
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "BuzzBuzz", "BuzzBuzz")

    def test_give_highest_number(self):
        num = 10000
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "BuzzBuzz", "BuzzBuzz")


class TestCasMod25And9(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 225
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    def test_give_middle_number(self):
        num = 5175
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    def test_give_highest_number(self):
        num = 9900
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")


class TestCaseNotMeetTheConditions(unittest.TestCase):
    def test_give_lowest_number(self):
        num = 1
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "NoFizzBuzz", "NoFizzBuzz")

    def test_give_middle_number(self):
        num = 5002
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "NoFizzBuzz", "NoFizzBuzz")

    def test_give_highest_number(self):
        num = 9998
        Superfizzbuzz = superfizzbuzz(num)
        self.assertEqual(Superfizzbuzz, "NoFizzBuzz", "NoFizzBuzz")
