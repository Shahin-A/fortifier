from unittest import TestCase

from parameterized import parameterized

from coding.string.parantheses import Parantheses

class TestParantheses(TestCase):

    p = Parantheses()

    @parameterized.expand([
        ["0", "(()", "()"],
        ["1", None, ""],
        ["2", "(()(()", "()"],
        ["2", "(()(())", "()(())"]
    ])
    def test_get_longest_parantheses(self, name, source, result):
        self.assertEqual(result, self.p.get_longest_parantheses(source))

    @parameterized.expand([
        ["0", "(()", 2],
        ["1", None, 0],
        ["2", "(()(()()", 4],
        ["2", "(()(())", 6]
    ])
    def test_get_longest_parantheses(self, name, source, result):
        self.assertEqual(result, self.p.get_longest_parantheses_length(source))
