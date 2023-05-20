"""
https://leetcode.com/problems/evaluate-division/
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
"""
from collections import defaultdict
from typing import List, Set, DefaultDict, Dict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        answers: List[float] = [0] * len(queries)

        def dfs(a: str, b: str, product: float, visited: Set[str]) -> float:
            if b in graph[a]:
                # Find the path to b
                return graph[a][b] * product
            # For each unvisited path in graph[a] find the path to b
            for k, weight in graph[a].items():
                if k in visited:
                    continue
                copied = visited.copy()
                copied.add(k)
                result = dfs(k, b, product * weight, copied)
                if result > -1:
                    # Find the path to b
                    return result
            # Couldn't reach b
            return -1.0

        # Create a graph
        graph: DefaultDict[str, Dict[str, float]] = defaultdict(dict)
        for e, v in zip(equations, values):
            a, b = e
            graph[a][b] = v
            graph[b][a] = 1 / v

        for i, query in enumerate(queries):
            a, b = query
            if a not in graph or b not in graph:
                answers[i] = -1.0
            else:
                answers[i] = dfs(a, b, 1, set([a]))

        return answers
