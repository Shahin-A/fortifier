class Matrix:

    def __init__(self, arr):
        self.arr = arr

    def rotate(self):
        """
        Divide the matrix into 4 pieces of non overlapping rectangles. In this case the range would be (n+1)/2 and n/2.
        The rotation follows below order:
        (i, j) -> (j, n-i-1) -> (n-i-1, n-j-1) -> (n-j-1, i) -> (i, j)
        :return:
        """
        if not self.arr or len(self.arr) == 0 or len(self.arr[0]) == 0:
            return None
        n = len(self.arr)
        i_range = (n + 1) / 2
        j_range = n / 2
        for i in range(i_range):
            for j in range(j_range):
                complement_i = n - i - 1
                complement_j = n - j - 1
                self.arr[i][j], self.arr[j][complement_i], self.arr[complement_i][complement_j], self.arr[complement_j][i] = \
                    self.arr[complement_j][i], self.arr[i][j], self.arr[j][complement_i], self.arr[complement_i][complement_j]
        return self