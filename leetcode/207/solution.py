"""
https://leetcode.com/problems/course-schedule/
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
from typing import List, DefaultDict
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0: haven't been visited
        # 1: is now been visited -> if seen[i]==1, then we detected a loop
        # 2: done traversing
        seen = [0] * numCourses

        # Create a graph
        graph: DefaultDict[int, List[int]] = defaultdict(list)
        for a, b in prerequisites:
            # Shortcut
            if a == b or b in graph[a]:
                return False
            graph[b].append(a)

        def dfs(i: int) -> bool:
            if seen[i] == 2:  # Already visited
                return True
            if seen[i] == 1:  # Detected a loop
                return False

            seen[i] = 1  # Mark as being visited
            for j in graph[i]:
                if not dfs(j):
                    return False

            seen[i] = 2  # Mark as done
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
