from unittest import TestCase
from parameterized import parameterized

from coding.dp.edit_distance import EditDistance

class TestEditDistance(TestCase):

    ed = EditDistance()

    @parameterized.expand([
        ["0", "", "abc", 3],
        ["1", "hello", "", 5],
        ["2", "horse", "rose", 2]
    ])
    def test_edits(self, name, source, target, result):
        self.assertEqual(result, self.ed.edits(source, target))