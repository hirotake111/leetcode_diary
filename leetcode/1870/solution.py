"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
1870. Minimum Speed to Arrive on Time
"""
from typing import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # Edge case
        if ceil(hour) < len(dist):
            return -1

        def validate(speed: int) -> bool:
            total = sum(ceil(km / speed) for km in dist[:-1]) + dist[-1] / speed
            return total <= hour

        l, r = 1, 10**7
        while l < r:
            m = (l + r) // 2
            if validate(m):
                # Possibly there is lower speed we can achieve with
                r = m
            else:
                # We need to increment speed
                l = m + 1

        return l
