"""
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/
2328. Number of Increasing Paths in a Grid

You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.
"""
from typing import List
from functools import lru_cache


class Solution:
    """DFS + cache approach"""

    def countPaths(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            result = 1
            for row, col in [(i + row, j + col) for row, col in directions]:
                if 0 <= row < m and 0 <= col < n and grid[i][j] < grid[row][col]:
                    result += dfs(row, col) % MOD
            return result % MOD

        return sum(dfs(row, col) % MOD for col in range(n) for row in range(m)) % MOD
        # total = 0
        # for row in range(m):
        #    total += sum(dfs(row, col) % MOD for col in range(n))
        # return total % MOD
