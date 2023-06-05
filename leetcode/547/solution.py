"""
https://leetcode.com/problems/number-of-provinces/
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.roots = [i for i in range(n)]

    def find(self, i: int):
        if self.roots[i] != i:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]

    def union(self, i: int, j: int):
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            pass
        if root_j < root_i:
            i, j = j, i
            root_i, root_j = root_j, root_i
        self.roots[i] = root_j
        return self.roots[i]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        s = set()
        for x in uf.roots:
            s.add(uf.find(x))
        return len(s)
