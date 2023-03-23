"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
1319. Number of Operations to Make Network Connected

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
"""
from typing import List
from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """Union Find approach"""
        # If we don't have enough cables to connect all pcs, then return - 1
        if len(connections) < n - 1:
            return -1

        # Now we are sure that we can connect all the pcs with the cables we have.
        # And all we need to do is to find the number of islands
        roots = [i for i in range(n)]
        # All pcs are seen as island for the first time
        islands = set(roots)

        def find(i: int) -> int:
            if roots[i] == i:
                return i
            return find(roots[i])

        for a, b in connections:
            # Find
            root_a, root_b = find(a), find(b)
            # Swap if needed (root_a should be smaller number)
            if root_a > root_b:
                root_a, root_b = root_b, root_a
            # If both are the same, skip the rest
            if root_a == root_b:
                continue
            # Union
            roots[root_b] = root_a
            # Remove root_b if it's in the islands
            if root_b in islands:
                islands.remove(root_b)

        # In order to connect all islands, we need (islands - 1) cables
        return len(islands) - 1

        """DFS approach"""
        # # Shortcut
        # # If we don't have enough cables to connect all pcs,
        # # then return -1
        # if len(connections) < n - 1:
        # return -1

        # """
        # At this point we are sure that we can connect all the pcs with ethernet cables we have.
        # And all we need to do is to find the number of islands
        # """
        # # Create a graph
        # graph = defaultdict(list)
        # for a, b in connections:
        # graph[a].append(b)
        # graph[b].append(a)

        # seen, islands = set(), 0

        # def dfs(i: int):
        # seen.add(i)
        # for pc in graph[i]:
        # if pc in seen:
        # continue
        # # Go to the next recursively
        # dfs(pc)

        # for pc in range(n):
        # if pc in seen:
        # # This pc is in the previous existing island
        # continue
        # # New islands -> mark it as 1
        # islands += 1
        # dfs(pc)

        # # In order to connect all islands, we need (islands - 1) cables
        # return islands - 1
