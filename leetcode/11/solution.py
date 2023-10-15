"""
https://leetcode.com/problems/container-with-most-water/
11. Container With Most Water
"""
from unittest import main, TestCase
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            # calc area
            area = min(height[i], height[j]) * (j - i)
            # update max_area
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # self.assertEqual(self.s.maxArea([1, 1]), 1)
        self.assertEqual(self.s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


if __name__ == "__main__":
    main()
