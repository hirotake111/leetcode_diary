"""
https://leetcode.com/problems/3sum-with-multiplicity/
923. 3Sum With Multiplicity

Given an integer array arr, and an integer target, 
return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
Constraints:
3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr = list(filter(lambda x: x >= target, sorted(arr)))
        l = len(arr)
        ans = 0

        def func(summary: int, idx: int):
            for i in range(idx, l):
                tmp = summary + arr[i]
                if tmp == target:
                    ans += 1

        func(0, 0)

        return ans
