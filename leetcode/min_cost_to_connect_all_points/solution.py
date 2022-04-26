from typing import Any, Dict, List, Set, Tuple
from unittest import main, TestCase


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]

    def find(self, n: int) -> int:
        if self.parent[n] == n:
            # n is root
            return n
        return self.find(self.parent[n])

    def union(self, n1, n2) -> bool:
        pn1, pn2 = self.find(n1), self.find(n2)
        if pn1 == pn2:
            return False
        # else, union group
        self.parent[pn1] = pn2
        return True


def get_distance(a: List[int], b: List[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create a list of elements (weight, edge1, edge2)
        edges: List[Tuple[int, int, int]] = []
        l = len(points)
        for i in range(l):
            for j in range(i + 1, l):
                edges.append((get_distance(points[i], points[j]), i, j))

        # sort edges by its weight
        edges.sort(key=lambda x: x[0])

        # populate cost of the MST
        uf = UnionFind(l)
        edges_used = 0
        cost = 0
        for w, node1, node2 in edges:
            if edges_used == l - 1:
                # we have already created MST
                break
            if not uf.union(node1, node2):
                # this edge makes a circle -> we will not add this edge to the cost
                continue
            cost += w
            edges_used += 1

        return cost


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(self.s.minCostConnectPoints(points), 20)
        points = [[3, 12], [-2, 5], [-4, 1]]
        self.assertEqual(self.s.minCostConnectPoints(points), 18)
        points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]
        self.assertEqual(self.s.minCostConnectPoints(points), 53)
        points = [[-14, -14], [-18, 5], [18, -10], [18, 18], [10, -2]]
        self.assertEqual(self.s.minCostConnectPoints(points), 102)


if __name__ == "__main__":
    main()
