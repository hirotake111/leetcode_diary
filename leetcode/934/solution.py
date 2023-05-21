"""
https://leetcode.com/problems/shortest-bridge/description/
934. Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.
"""
from typing import List, Deque, Tuple
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        DFS + BFS approach
        1. Find a cell that belongs to either of island
        2-1. Use DFS to identify all the cells for the island
        2-2. Also identify all water cells surfacing the island, and push them to queue
        3. Use BFS to identify the shortest path
        """
        n = len(grid)
        queue: Deque[Tuple[int, int]] = deque()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def dfs(a: int, b: int):
            for row, col in directions:
                row, col = row + a, col + b
                if row < 0 or n <= row or col < 0 or n <= col:
                    continue
                if grid[row][col] == 0:
                    # Enqueue
                    grid[row][col] = -1
                    queue.append((row, col))
                    continue
                if grid[row][col] == 1:
                    # Keep digging the island
                    grid[row][col] = 2
                    dfs(row, col)

        # Find a cell
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:  # Found it!
                    grid[i][j] = 2
                    break
            if grid[i][j] == 2:
                break

        # Use DFS to identify all the cell for the island
        # Also identify all water cells surfacing the island, and push them to queue
        dfs(i, j)

        # Use BFS to identify the shortest path
        answer = 0
        while queue:
            a, b = queue.popleft()
            # Traverse each direction
            for row, col in directions:
                row, col = row + a, col + b
                if row < 0 or n <= row or col < 0 or n <= col:
                    # Out of bound
                    continue
                if grid[row][col] == 1:
                    # We found one!
                    answer = grid[a][b]
                    break
                if grid[row][col] == 0:
                    # Another water cell -> continue to search
                    grid[row][col] = grid[a][b] - 1
                    queue.append((row, col))

            if answer != 0:
                break

        return -answer
