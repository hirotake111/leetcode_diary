from functools import lru_cache
from typing import Tuple, Union
from unittest import TestCase, main
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        DP approach

        - The tricky part is to handle three things - the starting point of nums, the ending point of nums, and the current point of multpliers.

        - If we go for a 3D DP solution, it will be TLE given the constrains. Hense we need to reduce it to a 2D solution.

        - Suppose our current index of multiplier is i and our starting point of nums is j, then the ending point would be at index "n - 1 - i + j".
        """
        n, m = len(nums), len(multipliers)

        @lru_cache
        def dfs(i: int, j: int):
            if m <= i:
                return 0

            left = dfs(i + 1, j + 1) + multipliers[i] * nums[j]
            right = dfs(i + 1, j) + multipliers[i] * nums[n - 1 - i + j]
            return max(left, right)

        return dfs(0, 0)


class Test(TestCase):
    data: List[Tuple[List[int], List[int], int]] = [
        ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102),
    ]

    def test_solution(self):
        s = Solution()
        for nums, multipliers, expected in self.data:
            self.assertEqual(s.maximumScore(nums, multipliers), expected)


if __name__ == "__main__":
    main()

"""

"""
