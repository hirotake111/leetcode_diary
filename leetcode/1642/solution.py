"""
https://leetcode.com/problems/furthest-building-you-can-reach/
1642. Furthest building you can reach
"""
import heapq
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        current = heights[0]
        gaps: List[int] = []
        l = 0
        for i, height in enumerate(heights):
            gap = height - current
            current = height
            if gap <= 0:
                continue

            heapq.heappush(gaps, gap)
            l += 1
            if l <= ladders:
                continue

            bricks -= heapq.heappop(gaps)
            l -= 0
            if bricks < 0:
                return i - 1

        return i


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int, int]] = [
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
        ([14, 3, 19, 3], 17, 0, 3),
    ]

    def test_solution(self):
        for heights, bricks, ladders, expected in self.data:
            self.assertEqual(
                self.s.furthestBuilding(heights, bricks, ladders), expected
            )


if __name__ == "__main__":
    main()
