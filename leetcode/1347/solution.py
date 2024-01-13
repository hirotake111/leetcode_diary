"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-05
1347. Minimum Number of Steps to Make Two Strings Anagram
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = [0] * 26, [0] * 26
        for c in s:
            cs[ord(c) - 97] += 1
        for c in t:
            ct[ord(c) - 97] += 1
        return sum([max(ct[i] - cs[i], 0) for i in range(26)])
