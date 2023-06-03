"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
1376. Time Needed to Inform All Employees

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
"""
from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        # Create a graph
        graph = defaultdict(list)
        for e, m in enumerate(manager):
            graph[m].append(e)

        # DFS approach
        def dfs(i: int, minutes: int) -> int:
            if len(graph[i]) == 0:
                return minutes
            return max([dfs(j, minutes + informTime[i]) for j in graph[i]])

        return dfs(headID, 0)

        # BFS approach
        # queue = deque()
        # max_value = 0
        # queue.append((headID, 0))
        # while queue:
        #    man, minutes = queue.popleft()
        #    if len(graph[man]) == 0:
        #        max_value = max(max_value, minutes)
        #    else:
        #        for sub in graph[man]:
        #            queue.append((sub, minutes + informTime[man]))

        # return max_value
