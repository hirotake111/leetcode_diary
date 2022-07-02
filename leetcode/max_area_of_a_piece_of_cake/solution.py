from heapq import heapify, heappop
from mailcap import findmatch
from typing import List, Set, Tuple
from unittest import TestCase, main


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        def find_max(arr: List[int], edge: int):
            max_length, prev = 0, 0
            heapify(arr)
            while arr:
                elm = heappop(arr)
                max_length = max(max_length, elm - prev)
                prev = elm
            return max(max_length, edge - prev)

        max_h = find_max(horizontalCuts, h)
        max_w = find_max(verticalCuts, w)

        return (max_h * max_w) % 1000000007


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int, List[int], List[int], int]] = [
        (5, 4, [1, 2, 4], [1, 3], 4),
        (5, 4, [3, 1], [1], 6),
        (5, 4, [3], [3], 9),
    ]

    def test_solution(self):
        for h, w, h_cuts, v_cuts, expected in self.data:
            self.assertEqual(self.s.maxArea(h, w, h_cuts, v_cuts), expected)


if __name__ == "__main__":
    main()
