"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
1930. Unique Length-3 Palindromic Subsequences
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(s)
        total = 0
        for c in chars:
            i, j = s.index(c), s.rindex(c)
            middles = s[i + 1 : j]
            total += len(set(middles))

        return total
