"""
https://leetcode.com/problems/flip-string-to-monotone-increasing/
926. Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left = 0  # num of ones on the left window
        right = s.count("0")  # num of zeroes on the right window
        answer = right

        for n in s:
            if n == "0":
                # decrease right window
                right -= 1
            else:
                # n == 1 -> increase left window
                left += 1
            answer = min(answer, left + right)

        return answer
