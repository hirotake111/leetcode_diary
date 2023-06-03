"""
https://leetcode.com/problems/detonate-the-maximum-bombs/
2101. Detonate the Maximum Bombs

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
"""
from typing import List, Set
from collections import defaultdict
import math


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Create a graph
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)

        def dfs(i: int, visited: Set[int]) -> int:
            if i in visited:
                return 0
            visited.add(i)
            for j in graph[i]:
                dfs(j, visited)
            return len(visited)

        # Traverse the created graph and found out max value
        return max([dfs(i, set()) for i in range(len(bombs))])
        # max_value = 0
        # for i in range(l):
        #    max_value = max(max_value, dfs(i, set()))
        # return max_value
