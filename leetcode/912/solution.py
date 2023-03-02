"""
https://leetcode.com/problems/sort-an-array/
912. Sort an Array
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Merge sort approach"""
        return self.merge_sort(nums)

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left, right = self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:])

        i = j = k = 0
        while k < len(arr):
            if len(left) <= i:
                arr[k] = right[j]
                j += 1
            elif len(right) <= j:
                arr[k] = left[i]
                i += 1
            elif left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        return arr
