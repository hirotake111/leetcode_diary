"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        n = min(l1, l2)

        while n:
            if l1 % n or l2 % n:
                # not divisible -> go to the next
                n -= 1
                continue
            base = str1[:n]
            if self.valid_gcd(base, str1) and self.valid_gcd(base, str2):
                break
            n -= 1

        return str1[:n]

    def valid_gcd(self, base: str, s: str) -> bool:
        l = len(s) // len(base)
        return s == base * l
