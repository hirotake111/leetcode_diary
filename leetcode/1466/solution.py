"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
1466. Reorder Routes to Make All Paths Lead to the City Zero
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""
from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """DFS approach"""
        # Create a graph
        # We will add a->b and b->a, with cost
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        def dfs(city: int, prev: int) -> int:
            changes = 0
            for next, cost in graph[city]:
                # If this is not the previous one, adds up changes
                if next != prev:
                    changes += cost + dfs(next, city)
            return changes

        return dfs(0, -1)
