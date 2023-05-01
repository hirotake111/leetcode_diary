"""
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

1579. Remove Max Number of Edges to Keep Graph Fully Traversable

Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [type_i, ui, vi] represents a bidirectional edge of type type_i between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
"""
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        answer = 0
        uf_a, uf_b = UnionFind(n), UnionFind(n)

        # Sort edges by its type in descending order
        # So that we will process edges with type 3 -> 2 -> 1
        # (Otherwise it would be complicated in determining which edge to be deleted)
        for t, u, v in sorted(edges, reverse=True):
            u, v = u - 1, v - 1
            if t == 3:  # Alice and Bob
                answer += uf_a.union(u, v) | uf_b.union(u, v)
            elif t == 2:  # Bob only
                answer += uf_b.union(u, v)
            else:  # Alice only
                answer += uf_a.union(u, v)
        # Both uf.count should be 1, otherwise, return -1
        if uf_a.count == 1 and uf_b.count == 1:
            return answer
        return -1


class UnionFind:
    def __init__(self, n: int):
        self.roots = list(range(n))
        self.count = n

    def find(self, idx: int) -> int:
        if self.roots[idx] != idx:
            self.roots[idx] = self.find(self.roots[idx])
        return self.roots[idx]

    def union(self, i: int, j: int) -> int:
        """Returns the num of edges to be removed (that is, either 1 or 0)"""
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            # Two have already got connected
            return 1
        self.count -= 1
        if root_j < root_i:
            root_i, root_j = root_j, root_i
        self.roots[root_j] = root_i
        return 0
