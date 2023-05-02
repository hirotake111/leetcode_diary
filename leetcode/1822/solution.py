"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/
1822. Sign of the Product of an Array

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_negative = False
        for i in nums:
            if i == 0:
                return 0
            is_negative ^= i < 0
        return -1 if is_negative else 1
