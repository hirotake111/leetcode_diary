"""
https://leetcode.com/problems/count-ways-to-build-good-strings/description/
2466. Count Ways To Build Good Strings

Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """Bottom up DP approach"""
        dp = [0] * (high + 1)
        dp[high] = 1
        mod = 10**9 + 7

        for i in range(high - 1, -1, -1):
            if low <= i:
                dp[i] += 1
            if i + zero <= high:
                dp[i] = (dp[i] + dp[i + zero]) % mod
            if i + one <= high:
                dp[i] = (dp[i] + dp[i + one]) % mod

        return dp[0] % mod
