"""
980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/
"""
from typing import List, Tuple, Set
from unittest import TestCase, main


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start: Tuple[int, int]
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        empties = 1
        answer = 0

        # Find starting square
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 0:
                    empties += 1

        def dfs(x: int, y: int, grid: List[List[int]], visited: int):
            if grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                if visited == empties:
                    answer += 1
                else:
                    return
            # Mark (x, y) as visited
            grid[x][y] = -1
            # Go to the next directions
            for a, b in directions:
                if 0 <= x + a < m and 0 <= y + b < n:
                    dfs(x + a, y + b, grid.copy(), visited + 1)

        dfs(start[0], start[1], grid.copy(), 0)
        return answer


class Test(TestCase):
    data: List[Tuple[List[List[int]], int]] = [
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.uniquePathsIII(input), expected)


if __name__ == "__main__":
    main()
