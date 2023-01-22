"""
https://leetcode.com/problems/palindrome-partitioning/
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
"""
from typing import List, Tuple
from unittest import TestCase, main
from functools import lru_cache


"""
Backtrack + Dynamic Programming approach
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def valid_palindrome(s: str) -> bool:
            return s != "" and s == s[::-1]

        @lru_cache()
        def backtrack(i: int) -> List[List[str]]:
            arr: List[List[str]] = []
            if len(s[i:]) == 0:
                # No more strings to be processed -> return empty array
                return [[]]

            if len(s[i:]) == 1:
                # Only one character -> return it
                return [[s[i]]]

            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if valid_palindrome(substring):
                    for palindromes in backtrack(j):
                        arr.append([substring] + palindromes)

            return arr

        return backtrack(0)


class Test(TestCase):
    data: List[Tuple[str, List[List[str]]]] = [
        ("bb", [["b", "b"], ["bb"]]),
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
    ]

    def test_solution(self):
        solution = Solution()
        for s, expected in self.data:
            self.assertEqual(solution.partition(s), expected)


if __name__ == "__main__":
    main()
