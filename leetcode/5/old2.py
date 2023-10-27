from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def func(left: int, right: int, longest: str) -> str:
            """returns the longest palindromic substring using left and right index"""
            longest_length = len(longest)
            while 0 <= left and right < l and s[left] == s[right]:
                length = right - left + 1
                if longest_length < length:
                    longest = s[left : right + 1]
                    longest_length = length
                left -= 1
                right += 1
            return longest

        l = len(s)
        longest = s[0]

        for i in range(l):
            longest = func(i - 1, i + 1, longest)
            longest = func(i, i + 1, longest)

        return longest


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, str]] = [
        ("cbbd", "bb"),
        ("aaaa", "aaaa"),
        ("babad", "bab"),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.longestPalindrome(input), expected)


if __name__ == "__main__":
    main()
