"""
https://leetcode.com/problems/find-eventual-safe-states/
802. Find Eventual Safe States
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        seen = [False] * len(graph)

        def dfs(i: int) -> bool:
            if len(graph[i]) == 0:
                # Found a terminal node
                safe_nodes.add(i)
                return True

            is_safe = True
            for j in graph[i]:
                if j in safe_nodes:
                    # Do nothing and continue traversing child nodes
                    continue
                elif seen[j]:
                    # Visited before but not a safe node
                    # -> node i will also be an unsafe node
                    is_safe = False
                else:
                    # j hasn't been seen -> traverse it
                    seen[j] = True
                    is_safe &= dfs(j)

            if is_safe:
                safe_nodes.add(i)
            return is_safe

        for k in range(len(graph)):
            seen[k] = True
            dfs(k)

        return sorted(safe_nodes)
