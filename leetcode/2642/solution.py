"""
https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
2642. Design Graph With Shortest Path Calculator
"""
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.max = 1_000_001 * n
        for frm, to, cost in edges:
            self.graph[frm].append((cost, to))

    def addEdge(self, edge: List[int]) -> None:
        frm, to, cost = edge
        self.graph[frm].append((cost, to))

    def shortestPath(self, node1: int, node2: int) -> int:
        costs = defaultdict(lambda: self.max)
        seen = set()
        heap = [(0, node1)]

        while heap:
            cost, i = heappop(heap)
            if i == node2:
                # found the answer
                return cost
            # update costs[i] (min cost from node1 to i)
            costs[i] = min(costs[i], cost)
            # if we haven't visited i, then enqueue subsequent edges
            if i in seen:
                continue
            seen.add(i)
            for additional_cost, j in self.graph[i]:
                if j not in seen:
                    heappush(heap, (additional_cost + cost, j))

        return -1
