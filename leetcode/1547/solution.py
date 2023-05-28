"""
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
1547. Minimum Cost to Cut a Stick
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
You should perform the cuts in order, you can change the order of the cuts as you wish.
The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.
Return the minimum total cost of the cuts.
"""
from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        MAX = 10**6 * len(cuts) + 1

        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if right - left == 1:
                return 0

            min_cost = MAX
            for pos in cuts:
                if pos <= left or right <= pos:
                    continue

                cost = right - left
                a = dfs(left, pos)
                b = dfs(pos, right)
                min_cost = min(min_cost, a + b + cost)

            return 0 if min_cost == MAX else min_cost

        return dfs(0, n)
