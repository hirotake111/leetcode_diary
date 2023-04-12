"""
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
1857. Largest Color Value in a Directed Graph

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
"""
from typing import List, Dict, Set, Tuple
from unittest import TestCase, main


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        answer = 0
        # Create a graph
        # graph = defaultdict(list)
        graph: Dict[int, List[int]] = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)

        memo: Dict[int, int] = {}

        def traverse(i: int, scores: List[int], seen: Set[int]) -> int:
            if i in seen:
                return -1

            if i in memo:
                return memo[i]

            scores[(ord(colors[i]) - 97)] += 1
            seen.add(i)

            if i not in graph:
                return max(scores)

            new_score = 0
            for node in graph[i]:
                tmp = traverse(node, scores.copy(), seen.copy())
                if tmp == -1:
                    return -1
                new_score = max(new_score, tmp)

            memo[i] = new_score
            return new_score

        for a in graph.keys():
            score = traverse(a, [0] * 26, set())
            if score == -1:  # Found loop
                return -1
            answer = max(answer, score)

        return answer


class Test(TestCase):
    test_cases: List[Tuple[str, List[List[int]], int]] = [
        ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3),
        # ("a", [[0, 0]], -1),
    ]

    def test_solution(self):
        solution = Solution()
        for colors, edges, expected in self.test_cases:
            self.assertEqual(solution.largestPathValue(colors, edges), expected)


if __name__ == "__main__":
    main()
