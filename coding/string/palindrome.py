
class Palindrome:

    def get_longest_palindrome(self, s):
        if not s:
            return ""
        max_palindrome = ""
        for i in range(len(s)):
            even_palindrome = self.__get_max_even_palindrome(s, i)
            odd_palindrome = self.__get_max_odd_palindrome(s, i)
            max_palindrome = max(max_palindrome, even_palindrome, odd_palindrome, key=lambda x: len(x))
        return max_palindrome

    def __get_max_even_palindrome(self, s, i):
        window = min(i, len(s) - i)
        left, right = i - 1, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def __get_max_odd_palindrome(self, s, i):
        window = min(i, len(s) - i - 1)
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]