"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
2492. Minimum Score of a Path Between Two Cities
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
"""
from collections import defaultdict
from typing import List

MAX_DISTANCE = 100005


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """DFS approach"""
        # Create a graph
        graph = defaultdict(list)
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = set([1])

        def dfs(a: int, min_distance: int) -> int:
            for b, distance in graph[a]:
                min_distance = min(min_distance, distance)
                if b not in visited:
                    # Mark a as visited
                    visited.add(b)
                    min_distance = min(min_distance, dfs(b, min_distance))
            return min_distance

        return dfs(1, MAX_DISTANCE)
