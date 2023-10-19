"""
https://leetcode.com/problems/parallel-courses-iii/
2050. Parallel Courses III
"""
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for child, parent in relations:
            graph[parent - 1].append(child - 1)

        @lru_cache(None)
        def dfs(parent: int) -> int:
            if len(graph[parent]) == 0:
                return time[parent]
            return time[parent] + max(dfs(ch) for ch in graph[parent])

        return max(dfs(i) for i in range(n))
