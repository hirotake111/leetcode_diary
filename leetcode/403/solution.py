"""
https://leetcode.com/problems/frog-jump/
403. Frog Jump
"""
from typing import List
from functools import lru_cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last_index = len(stones) - 1

        @lru_cache(None)
        def dfs(i: int, prev_v: int) -> bool:
            if i == last_index:
                return True

            j = i + 1
            while j <= last_index:
                current_v = stones[j] - stones[i]
                # If current velocity is more than (prev velocity + 1),
                # then we no longer need to search stones anymore
                if current_v > prev_v + 1:
                    break
                # If current velocity is within +- prev velocity, then traverse the next stone.
                # If dfs(...) is True, then also return true
                if current_v in (prev_v, prev_v - 1, prev_v + 1) and dfs(j, current_v):
                    return True
                j += 1
            return False

        return dfs(0, 0)
