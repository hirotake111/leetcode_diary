"""
2279. Maximum Bags With Full Capacity of Rocks
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
"""
from typing import List


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        answer = 0
        for value in sorted([c - r for c, r in zip(capacity, rocks)]):
            if additionalRocks < value:
                break
            additionalRocks -= value
            answer += 1

        return answer
