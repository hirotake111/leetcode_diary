"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
1561. Maximum Number of Coins You Can Get
"""


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        t = math.ceil(len(piles) / 3)
        return sum(piles[i - 1] for i in range(len(piles) - 1, t, -2))
