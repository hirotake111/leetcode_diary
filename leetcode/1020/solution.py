"""
https://leetcode.com/problems/number-of-enclaves/
1020. Number of Enclaves

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
"""

from typing import List, Deque, Tuple
from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """BFS approach"""
        m, n = len(grid), len(grid[0])
        queue: Deque[Tuple[int, int]] = deque()

        # Traverse the grid's boundaries and push elements if value is 1
        x = 0
        for y in range(n):
            if grid[x][y] == 1:
                grid[x][y] = 0
                queue.append((x, y))

        y = n - 1
        for x in range(m):
            if grid[x][y] == 1:
                grid[x][y] = 0
                queue.append((x, y))

        x = m - 1
        for y in range(n):
            if grid[x][y] == 1:
                grid[x][y] = 0
                queue.append((x, y))

        y = 0
        for x in range(m):
            if grid[x][y] == 1:
                grid[x][y] = 0
                queue.append((x, y))

        # Mark all 1s to 0s
        while queue:
            a, b = queue.popleft()
            for x, y in ((a, b - 1), (a + 1, b), (a, b + 1), (a - 1, b)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 0
                    queue.append((x, y))

        return sum([sum(row) for row in grid])

        # """DFS approach"""
        # m, n = len(grid), len(grid[0])

        # def dfs(x: int, y: int):
        # grid[x][y] = 0
        # for a, b in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)):
        # if 0 <= a < m and 0 <= b < n and grid[a][b]:
        # dfs(a, b)

        # x = 0
        # for y in range(n):
        # if grid[x][y] == 1:
        # dfs(x, y)

        # y = n - 1
        # for x in range(m):
        # if grid[x][y] == 1:
        # dfs(x, y)

        # x = m - 1
        # for y in range(n):
        # if grid[x][y] == 1:
        # dfs(x, y)

        # y = 0
        # for x in range(m):
        # if grid[x][y] == 1:
        # dfs(x, y)

        # return sum([sum(row) for row in grid])
