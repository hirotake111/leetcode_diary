"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
1443. Minimum Time to Collect All Apples in a Tree
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.
"""
from typing import List, Tuple
from unittest import TestCase, main

"""
Approach: Backtracking
1. Let's make another array out of `edges` and call it `graph`, where each element `graph[i]` contains neighbour edge [a, b].
2. We can do DFS + backtracking to calculate the minimum time in second using `graph`.
"""


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Edge case: no apples - just return 0
        if len(list(filter(lambda edge: edge, hasApple))) == 0:
            return 0

        # Create a graph using edges
        graph: List[List[int]] = [[] for _ in range(n)]
        for a, b in edges:
            if b not in graph[a]:
                graph[a].append(b)
            if a not in graph[b]:
                graph[b].append(a)

        def dfs(idx: int, parent_idx: int) -> int:
            """
            idx: index of the current edge.
            parent_idx: index of the parent edge. We can use it to prevent going back to the parent.
            """
            sub_total = 0

            for edge_idx in graph[idx]:
                # If child == parent, do nothing to prevent going back to the parent
                # If not, this should be an index of a child edge
                if edge_idx != parent_idx:
                    sub_total += dfs(edge_idx, idx)

            # If the edge has apples in it, or  if children has apples,
            # we need to visit it -> add extra 2
            if hasApple[idx] or 0 < sub_total:
                return sub_total + 2
            # Else, this edge has no apples, or no children that have apples.
            # So we don't have to visit this edge -> just return 0
            return 0

        # In this approach dfs() assumes there is always a parent edge connected to it.
        # But since root doesn't have it - the result has 2 extra unit of seconds.
        # Therefore subtract 2 from the result of dfs()
        return dfs(0, -1) - 2


class Test(TestCase):
    data: List[Tuple[int, List[List[int]], List[bool], int]] = [
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, True, True, False],
            8,
        )
    ]

    def test_solution(self):
        s = Solution()
        for n, edges, has_appple, expected in self.data:
            self.assertEqual(s.minTime(n, edges, has_appple), expected)


if __name__ == "__main__":
    main()
