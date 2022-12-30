"""
797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""
from typing import List, Set, Tuple
from unittest import TestCase, main


class Solution:
    answer: List[List[int]]

    def __init__(self) -> None:
        self.answer = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)  # The num of nodes

        def dfs(idx: int, path: List[int], visited: Set[int]):
            if idx in visited:
                # We already have visited this path -> do nothing
                return
            # New node -> add it to the path
            path.append(idx)
            visited.add(idx)
            if idx == n - 1:
                # Now we have the path form 0 to n - 1 -> add it to the answer
                self.answer.append(path)
                return
            # We still have some nodes to be visted
            for node in graph[idx]:
                dfs(node, path.copy(), visited.copy())

        dfs(0, [], set())
        return self.answer


class Test(TestCase):
    data: List[Tuple[List[List[int]], List[List[int]]]] = [
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.allPathsSourceTarget(input), expected)


if __name__ == "__main__":
    main()
