"""
https://leetcode.com/problems/can-place-flowers/
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Edge case
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0

        # Shortcut
        # (len(flowerbed) + 1) // 2 is the maximum number it can plant
        # ex: r=5 -> 3, l=6 -> 3, l=7 -> 4
        if (len(flowerbed) + 1) // 2 < n:
            return False

        count = i = 0
        flowerbed = [0] + flowerbed + [0]
        while i < len(flowerbed) - 2:
            if sum(flowerbed[i : i + 3]) == 0:
                # Mark 1 in the middle
                flowerbed[i + 1] = 1
                count, i = count + 1, i + 1
            if n <= count:
                return True
            i += 1
        return False
