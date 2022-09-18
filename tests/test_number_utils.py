from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [999, 456, 2156798456498756]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)