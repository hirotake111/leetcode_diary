"""
https://leetcode.com/problems/painting-the-walls/
2742. Painting the Walls
"""
from typing import List
from functools import lru_cache


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        MAX = 1000001

        @lru_cache(None)
        def dfs(i: int, remain: int) -> int:
            if remain <= 0:
                return 0
            if i == len(cost):
                return MAX * len(cost)

            take = cost[i] + dfs(i + 1, remain - 1 - time[i])
            not_take = dfs(i + 1, remain)
            return min(take, not_take)

        return dfs(0, len(cost))
