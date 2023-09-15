"""
https://leetcode.com/problems/reconstruct-itinerary/?envType=daily-question&envId=2023-09-14
332. Reconstruct Itinerary
"""
from typing import List, DefaultDict
from collections import defaultdict
import bisect


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph
        graph: DefaultDict[str, List[str]] = defaultdict(list)
        for f, t in tickets:
            bisect.insort(graph[f], t)
        count = sum(len(d) for d in graph.values())

        # Recursively search the graph
        def dfs(current: str, count: int) -> List[str]:
            if count == 0:
                return [current]

            for _ in range(len(graph[current])):
                dist = graph[current].pop(0)
                arr = dfs(dist, count - 1)
                if len(arr) > 0:
                    # We found the path
                    return [current] + arr
                else:
                    # Push back dist to the graph
                    graph[current].append(dist)
            # We couldn't find the path
            return []

        return dfs("JFK", count)
