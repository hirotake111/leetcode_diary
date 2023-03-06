"""
https://leetcode.com/problems/kth-missing-positive-number/
1539. Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # If k is less than or equal to arr[0], then return k
        if k <= arr[0] - 1:
            return k

        # There should be arr[0] - 1 missing numbers before the 1st element
        # For example, if arr=[3,4,5], then arr[0]-1 -> 2 missing elements
        # So decrement k by (arr[0] - 1)
        k, prev = k - arr[0] + 1, arr[0]
        for i in range(1, len(arr)):
            diff = arr[i] - prev - 1  # The num of missing numbers in between
            if k <= diff:
                return prev + k
            # Update k and prev
            k, prev = k - diff, arr[i]

        # The answer is beyond arr -> return the last element of arr + k
        return arr[-1] + k
