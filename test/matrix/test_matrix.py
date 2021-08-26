from unittest import TestCase

from parameterized import parameterized

from coding.matrix.matrix import Matrix

class TestMatrix(TestCase):

    @parameterized.expand([
        ["0", [[1]], [[1]]],
        ["0", [[1,2], [3,4]], [[3, 1], [4, 2]]],
    ])
    def test_rotate(self, name, arr, result):
        matrix = Matrix(arr)
        self.assertEqual(result, matrix.rotate().arr)