
class Parantheses:

    def get_longest_parantheses(self, s):
        """
        Return a longest parantheses sequence.
        :param s:
        :return:
        """
        if not s:
            return ''
        stack, longest, start, end = [], 0, -1, -1
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    if length >= longest:
                        longest = length
                        start, end = stack[-1], i
        return s[start+1: end+1]


    def get_longest_parantheses_length(self, s):
        if not s:
            return 0
        n = len(s)
        return max(self.__get_max_parantheses_one_direction(s, 0, n-1, 1), self.__get_max_parantheses_one_direction(s, n-1, 0, -1))

    def __get_max_parantheses_one_direction(self, s, i, j, direction):
        longest, left, right = 0, 0, 0
        while direction * (j-i) >= 0:
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, 2*left)
            elif direction * (right - left) > 0:
                left, right = 0, 0

            i += direction

        return longest
