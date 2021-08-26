from unittest import TestCase
from parameterized import parameterized

from coding.dp.longest_common_subsequence import LongestCommonSubsequence

class TestLongestCommonSubsequence(TestCase):
    lcd = LongestCommonSubsequence()

    @parameterized.expand([
        ["0", "", "abc", (0, "")],
        ["1", "abbbc", "abcbcaa", (4, "abbc")],
        ["2", "abccccd", "fdeccccabd", (5, "ccccd")]
    ])
    def test_subsequence(self, name, source, target, result):
        self.assertEqual(result, self.lcd.get_subsequence(source, target))