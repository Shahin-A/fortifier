from unittest import TestCase

from parameterized import parameterized

from coding.string.palindrome import Palindrome

class TestPalindrome(TestCase):

    palindrome = Palindrome()

    @parameterized.expand([
        ["0", "aabbc", "aa"],
        ["1", None, ""],
        ["2", "babad", "bab"]
    ])
    def test_get_max_palindrome(self, name, s, result):
        self.assertEqual(result, self.palindrome.get_longest_palindrome(s))