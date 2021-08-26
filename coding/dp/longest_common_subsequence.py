class LongestCommonSubsequence:

    def get_subsequence(self, source, target):
        if not source or not target:
            return 0, ""
        a = [[0 for _ in range(len(target)+1)] for _ in range(len(source)+1)]
        for i in range(1, len(source)+1):
            for j in range(1, len(target)+1):
                a[i][j] = 1 + a[i-1][j-1] if source[i - 1] == target[j - 1] else max(a[i-1][j], a[i][j-1])
        return a[i][j], self.__get_subsequence(a, source, target)

    def __get_subsequence(self, a, source, target):
        i, j, subsequence = len(source), len(target), ""
        while i > 0 and j > 0:
            if source[i-1] == target[j-1]:
                subsequence = source[i-1] + subsequence
                i, j = i-1, j-1
            elif a[i][j] == a[i-1][j]:
                i = i-1
            else:
                j = j-1
        return subsequence