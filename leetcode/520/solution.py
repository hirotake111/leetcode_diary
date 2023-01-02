"""
https://leetcode.com/problems/detect-capital/
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
"""
from typing import List, Tuple
from re import match
from unittest import TestCase, main
from string import ascii_uppercase


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] in ascii_uppercase:
            return bool(match(r"^[A-Z]+$", word) or match(r"^[A-Z][a-z]+$", word))

        return bool(match(r"^[a-z]+$", word))


class Test(TestCase):
    data: List[Tuple[str, bool]] = [
        ("ffffffffffffffffffffF", False),
        ("USA", True),
        ("FlaG", False),
        ("leetcode", True),
        ("Leetcode", True),
        ("LeetCode", False),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.detectCapitalUse(input), expected)


if __name__ == "__main__":
    main()
