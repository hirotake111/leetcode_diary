"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [from_i, to_i] represents a directed edge from node from_i to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = set(range(n))
        for _, vertex in edges:
            if vertex in vertices:
                vertices.remove(vertex)

        return list(vertices)
