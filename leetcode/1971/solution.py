"""
1971. Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""
from typing import List, Tuple
from unittest import TestCase, main


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))

    def find(self, a: int) -> int:
        """Returns the root value"""
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        # Now self.root[a] points to the current root edge
        return self.root[a]

    def union(self, a: int, b: int):
        """Unoins two nodes"""
        # Find the root of A and B
        root_a, root_b = self.find(a), self.find(b)
        # Always make root A smaller than root B
        if root_b < root_a:
            root_a, root_b = root_b, root_a
        # Update root of B to point the root of A
        # so that the two groups are now connected
        self.root[root_b] = root_a


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        uf = UnionFind(n)

        # Union
        for a, b in edges:
            uf.union(a, b)

        # Find
        return uf.find(source) == uf.find(destination)


class Test(TestCase):
    data: List[Tuple[int, List[List[int]], int, int, bool]] = [
        (
            10,
            [
                [0, 7],
                [0, 8],
                [6, 1],
                [2, 0],
                [0, 4],
                [5, 8],
                [4, 7],
                [1, 3],
                [3, 5],
                [6, 5],
            ],
            7,
            5,
            True,
        ),
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    ]

    def test_solution(self):
        s = Solution()
        for n, edges, source, destination, expected in self.data:
            self.assertEqual(s.validPath(n, edges, source, destination), expected)


if __name__ == "__main__":
    main()
