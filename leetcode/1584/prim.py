"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
1584. Min Cost to Connect All Points
"""
from typing import List, Tuple, Set
from heapq import heappush, heappop

#
# Prim's algorithm
#


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create a graph
        n = len(points)
        graph: List[List[Tuple]] = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                graph[i].append((distance, j))
                graph[j].append((distance, i))

        total = 0
        seen: Set[int] = set()
        heap = [(0, 0)]
        while len(seen) < n:
            # Pick up one with the minimum distance,
            distance, node = heappop(heap)
            if node in seen:
                # This edge will make a circle -> skip it
                continue
            seen.add(node)
            total += distance
            # Add all the path from current node
            for distance, next_node in graph[node]:
                if next_node not in seen:
                    heappush(heap, (distance, next_node))

        return total
