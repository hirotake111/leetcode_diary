"""
https://leetcode.com/problems/restore-the-array/description/
1416. Restore The Array

A program was supposed to print an array of integers.
The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.
"""


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """Dynamic programming approach"""
        length = len(s)
        dp = [0] * (length + 1)
        dp[length] = 1  # Base line

        for i in range(length - 1, -1, -1):
            if s[i] == "0":
                # Loading zero -> s[i] is invalid. We don't have to calculate further
                continue
            for j in range(i, length):
                n = int(s[i : j + 1])
                if k < n:
                    # Stop the iteration as we no longer need to proceed
                    break
                dp[i] = (dp[i] + dp[j + 1]) % 1000000007

        return dp[0] % 1000000007
