"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Assign the first l and r
        l, r = max(weights), sum(weights)
        if days == 1:
            return r
        if len(weights) == days:
            return l

        while True:
            cap = (r - l) // 2 + l
            if self.validate(weights, days, cap):
                # You can ship all package with the capacity of cap within the days
                # Update r
                r = cap
            else:
                # You cannot -> update l
                l = cap + 1

            if l == r:
                return r

    def validate(self, weights: List[int], days: int, cap: int) -> bool:
        current = cap
        for w in weights:
            if current < w:
                current = cap
                days -= 1
            current -= w
            if days < 1:
                return False
        return True


class Test(TestCase):
    cases: List[Tuple[List[int], int, int]] = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
    ]

    def test_solution(self):
        solution = Solution()
        for weights, days, expected in self.cases:
            self.assertEqual(solution.shipWithinDays(weights, days), expected)


if __name__ == "__main__":
    main()
