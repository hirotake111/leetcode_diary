"""
https://leetcode.com/problems/as-far-from-land-as-possible/
1162. As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

"""
from typing import List, Tuple, Deque
from collections import deque
from unittest import TestCase, main


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, summary = len(grid), sum([sum(row) for row in grid])
        visited: List[List[int]] = [[0] * n for _ in range(n)]
        directions: List[Tuple[int, int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        queue: Deque[Tuple[int, int]] = deque()

        # Edge cases
        if summary == 0 or summary == n**2:
            return -1

        # Enqueue all 1s
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = 1
                    queue.append((i, j))

        distance = -1
        while queue:
            # Update distance
            distance += 1
            # Pick up items only in current queue (as queue grows over the loop)
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(a + i, b + j) for (a, b) in directions]:
                    if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
                        # [row, col] is in the grid and We haven't visited yet.
                        # Add (x, y) to the queue and mark as visited
                        queue.append((x, y))
                        visited[x][y] = 1

        # the longest distance from an island to the nearest cell is "distance"
        return distance


class Test(TestCase):
    data: List[Tuple[List[List[int]], int]] = [
        ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4),
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], -1),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], -1),
    ]

    def test_solution(self):
        solution = Solution()
        for grid, expected in self.data:
            self.assertEqual(solution.maxDistance(grid), expected)


if __name__ == "__main__":
    main()
