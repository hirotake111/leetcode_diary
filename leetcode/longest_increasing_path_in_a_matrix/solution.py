from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cost_matrix = [[None] * n for _ in range(m)]
        directions: List[Tuple[int, int]] = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        for x in range(m):
            for y in range(n):
                cost = 0
                for dx, dy in directions:
                    if not 0 <= (x + dx) < m:
                        pass
        return 0


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int]] = [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
    ]

    def test(self):
        for matrix, expected in self.data:
            self.assertSetEqual(self.s.longestIncreasingPath(matrix=matrix), expected)


if __name__ == "__main__":
    main()
