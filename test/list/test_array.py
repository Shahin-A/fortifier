from unittest import TestCase

from parameterized import parameterized

from coding.list.array import Array

class TestArray(TestCase):
    arr = Array()

    @parameterized.expand([
        ["0",[1,2,3], 2],
    ])
    def test_max_water(self, name, height, result):
        self.assertEqual(result, self.arr.get_max_water(height))

    @parameterized.expand([
        ["0", [1, 2, 3], 0],
        ["1", [3, 2, 1], 0],
        ["2", [2, 0, 2, 1], 2],
    ])
    def test_trap_water(self, name, height, result):
        self.assertEqual(result, self.arr.trap_water(height))

    @parameterized.expand([
        ["0", [1, 2, -3], [[-3, 1, 2]]],
    ])
    def test_three_sum(self, name, arr, result):
        self.assertEqual(result, self.arr.three_sum(arr))

    @parameterized.expand([
        ["0", [1, 1, 2, 2, 2, 2, 3, 4], 4, [(1, 3), (2, 2)]],
    ])
    def test_three_sum(self, name, arr, target, result):
        self.assertEqual(result, self.arr.two_sum_sorted(arr, target))

    @parameterized.expand([
        ["0", [1], [[1]]],
        ["0", [1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]],
    ])
    def test_permute(self, name, arr, result):
        self.assertEqual(result, self.arr.permute(arr))

    @parameterized.expand([
        ["0", [1, -2, 3], 3],
        ["1", [], 0],
        ["2", [-2,1,-3,4,-1,2,1,-5,4], 6],
    ])
    def test_max_subarray(self, name, arr, result):
        self.assertEqual(result, self.arr.max_subarray(arr))