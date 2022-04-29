from typing import Dict, List, Tuple
from unittest import main, TestCase


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        0, 1: marked as visited
        """
        colors: Dict[int, int] = {}

        def dfs(idx: int, color: int) -> bool:
            if idx in colors:
                return colors[idx] == color
            colors[idx] = color

            for node in graph[idx]:
                if not dfs(node, abs(color - 1)):
                    return False
            return True

        for i in range(len(graph)):
            if i not in colors:
                if not dfs(i, 0):
                    return False
        return True


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        # self.assertEqual(self.s.isBipartite(graph), False)
        # graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        # self.assertEqual(self.s.isBipartite(graph), True)
        # graph = [
        #     [],
        #     [2, 4, 6],
        #     [1, 4, 8, 9],
        #     [7, 8],
        #     [1, 2, 8, 9],
        #     [6, 9],
        #     [1, 5, 7, 8, 9],
        #     [3, 6, 9],
        #     [2, 3, 4, 6, 9],
        #     [2, 4, 5, 6, 7, 8],
        # ]
        # self.assertEqual(self.s.isBipartite(graph), False)
        # graph = [[4], [], [4], [4], [0, 2, 3]]
        # """
        # 0
        # |
        # 4-2
        # |
        # 3
        # """
        # self.assertEqual(self.s.isBipartite(graph), True)
        graph = [[1], [0], [4], [4], [2, 3]]
        self.assertEqual(self.s.isBipartite(graph), True)


if __name__ == "__main__":
    main()
