from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        for i in range(l - 1, -1, -1):
            if i < l - 2:
                cost[i] = min(cost[i + 1], cost[i + 2]) + cost[i]
        return min(cost[0], cost[1])


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.minCostClimbingStairs(input), expected)


if __name__ == "__main__":
    main()
