"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/
847. Shortest Path Visiting All Nodes
"""
from typing import List
from collections import deque

"""
DFS approach
"""


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = deque([(i, 1 << i) for i in range(len(graph))])
        all_ones = (1 << len(graph)) - 1
        # This will be used to avoid visiting the same path
        visited = [{i} for i in range(len(graph))]

        steps = -1
        while queue:
            steps += 1
            for _ in range(len(queue)):
                i, mask = queue.popleft()
                for j in graph[i]:
                    new_mask = mask | 1 << j
                    if new_mask == all_ones:
                        # Found the shortest path
                        return steps + 1
                    if new_mask not in visited[j]:
                        visited[j].add(new_mask)
                        queue.append((j, new_mask))

        return 0
