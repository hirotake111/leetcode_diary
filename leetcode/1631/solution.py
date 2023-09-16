"""
https://leetcode.com/problems/path-with-minimum-effort/
1631. Path With Minimum Effort
Medium
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # top, right, bottom, left
        visited = [[False] * n for _ in range(m)]

        heap = [(0, 0, 0)]  # cost, row, col
        while len(heap):
            cost, row, col = heappop(heap)
            if visited[row][col]:
                continue
            visited[row][col] = True
            if row == m - 1 and col == n - 1:
                # we reached the goal
                return cost
            # Traverse 4 directions
            for next_row, next_col in ((row + a, col + b) for a, b in directions):
                if (
                    0 <= next_row < m
                    and 0 <= next_col < n
                    and not visited[next_row][next_col]
                ):
                    next_cost = max(
                        cost, abs(heights[row][col] - heights[next_row][next_col])
                    )
                    heappush(heap, (next_cost, next_row, next_col))

        return -1
