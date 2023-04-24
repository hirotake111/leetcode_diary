"""
https://leetcode.com/problems/last-stone-weight/description/
1046. Last Stone Weight
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
from typing import List
from bisect import insort


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            # Pick up two heaviest stones and calculate the diff between them
            diff = stones.pop() - stones.pop()
            # If diff is 0 (two stones are in the same weight) do nothing and go to next
            # If 0 < diff, we need to insert the diff into the array again
            # We can use binary search to identify the index for the diff to be inserted.
            if diff:
                insort(stones, diff)

        # The array has possibly no items in it.
        # If so, return 0
        return stones[0] if stones else 0
