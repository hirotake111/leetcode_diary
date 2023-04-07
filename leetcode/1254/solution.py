"""
https://leetcode.com/problems/number-of-closed-islands/
1254. Number of Closed Islands
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """DFS approach"""
        m, n = len(grid), len(grid[0])
        counts = 0

        def dfs(x: int, y: int) -> bool:
            grid[x][y] = 1
            surrounded = True

            if x in (0, m - 1) or y in (0, n - 1):
                surrounded = False
                # We need to move forward to mark all adjacent island 1

            for a, b in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)):
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 0:
                    surrounded &= dfs(a, b)
            return surrounded

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    counts += dfs(i, j)

        return counts
