"""
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
1697. Checking Existence of Edge Length Limited Paths

An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, dis_i] denotes an edge between nodes ui and vi with distance dis_i. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limit_j], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limit_j .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.
"""
from typing import List, Tuple


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        """Union & Find approach"""
        uf = UnionFind(n)
        answer = [False] * len(queries)

        # Sort by weight
        edgeList.sort(key=lambda x: x[2])
        # Sort by weight while keeping original index
        queries = sorted([limit, p, q, i] for i, (p, q, limit) in enumerate(queries))

        i = 0
        for limit, p, q, j in queries:
            # Pick up edge one by one and add it to our union find graph
            # until it exceeds query's limit
            while i < len(edgeList):
                u, v, w = edgeList[i]
                if limit <= w:
                    break
                uf.union(u, v)
                i += 1
            # If roots are the same, then we can say they are connected each other
            answer[j] = uf.find(p) == uf.find(q)

        return answer


class UnionFind:
    roots: List[int]

    def __init__(self, n: int):
        self.roots = list(range(n))

    def find(self, i: int) -> int:
        if self.roots[i] != i:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]

    def union(self, i: int, j: int):
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return
        if root_j < root_i:
            root_i, root_j = root_j, root_i
        self.roots[root_j] = root_i
