"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""
from typing import List, Deque, Tuple
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """BFS approach"""
        n = len(grid)
        queue: Deque[Tuple[int, int, int]] = deque()
        directions = (
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        )

        # Edge case
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        def valid_path(row: int, col: int) -> bool:
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        queue.append((-1, -1, 0))
        while queue:
            a1, b1, steps = queue.popleft()
            for row, col in [(a1 + a2, b1 + b2) for a2, b2 in directions]:
                if not valid_path(row, col):
                    continue
                if row == col == n - 1:
                    # Reached the goal!
                    return steps + 1
                grid[row][col] = 1
                queue.append((row, col, steps + 1))

        # Couldn't find the path to the goal
        return -1
