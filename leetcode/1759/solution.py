"""
https://leetcode.com/problems/count-number-of-homogenous-substrings/
1759. Count Number of Homogenous Substrings
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        total = count = 1
        MOD = 1000000007
        for i in range(1, len(s)):
            count = (count + 1) % MOD if s[i] == s[i - 1] else 1
            total = total + count
        return total % MOD
