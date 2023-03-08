"""
https://leetcode.com/problems/koko-eating-bananas/
875. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Binary search approach"""
        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            speed = (min_speed + max_speed) // 2
            hours = sum(math.ceil(bananas / speed) for bananas in piles)
            if hours <= h:
                max_speed = speed
            else:
                min_speed = speed + 1

        return min_speed
