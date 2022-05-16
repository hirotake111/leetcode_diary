from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """bfs approach"""
        n = len(grid)
        direction: List[Tuple[int, int]] = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        q: List[Tuple[int, int, int]] = [(0, 0, 1)]

        # edge cases
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        while q:
            (x, y, cost) = q.pop(0)
            if grid[x][y] == 1:
                continue

            if x == n - 1 and y == n - 1:
                return cost

            grid[x][y] = 1
            for a, b in direction:
                if 0 <= x + a < n and 0 <= y + b < n and grid[x + a][y + b] == 0:
                    q.append((x + a, y + b, cost + 1))

        return -1


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int]] = [
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.shortestPathBinaryMatrix(input), expected)


if __name__ == "__main__":
    main()
