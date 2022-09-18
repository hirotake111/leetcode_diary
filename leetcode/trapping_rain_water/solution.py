from tkinter import N
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def trap(self, height: List[int]) -> int:
        # dynamic programming approach
        n, answer = len(height), 0
        if not height:
            return 0

        left = [0] * n
        right = left.copy()

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        right[-1] = height[-1]
        for i in range(n - 1)[::-1]:
            right[i] = max(height[i], right[i + 1])

        for i in range(n):
            answer += min(left[i], right[i]) - height[i]

        return answer


class Test(TestCase):
    data: List[Tuple[List[int], int]] = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.trap(input), expected)


if __name__ == "__main__":
    main()
