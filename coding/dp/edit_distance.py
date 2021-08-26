class EditDistance:

    def edits(self, word1, word2):
        if not word1 or not word2:
            return len(word1) + len(word2)
        else:
            return self.__edits(word1, word2)


    def __edits(self, word1, word2):
        m, n = len(word1), len(word2)
        edit_distance = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1 , -1):
                right = edit_distance[i][j+1] if j+1 < n else m-i
                down = edit_distance[i+1][j] if i+1 < m else n-j
                diagonal = edit_distance[i+1][j+1] if i+1 < m and j+1 < n else (m-i-1) + (n-j-1)
                edit_distance[i][j] = diagonal if word1[i] == word2[j] else 1 + min(right, down, diagonal)
        return edit_distance[0][0]