"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
1584. Min Cost to Connect All Points
"""
from typing import List

#
# Krustel's algorithm with Union Find method
#


class UnionFind:
    def __init__(self, n: int):
        self.arr = [i for i in range(n)]
        self.edges = n - 1  # num of edges to be connected

    def find(self, i: int) -> int:
        return i if self.arr[i] == i else self.find(self.arr[i])

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        self.arr[root_b] = root_a
        self.edges -= 1
        return True

    def done(self) -> bool:
        return self.edges == 0


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create a graph
        arr = []
        m = len(points)
        for i in range(m):
            for j in range(i + 1, m):
                distance = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                arr.append((distance, i, j))
        arr.sort()

        # Use union & find to detect a circle
        uf, total = UnionFind(m), 0
        for distance, i, j in arr:
            made_no_circle = uf.union(i, j)
            if made_no_circle:
                total += distance
            if uf.done():
                # Shortcut
                break

        return total
