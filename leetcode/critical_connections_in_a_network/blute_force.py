from collections import defaultdict
from unittest import TestCase, main
from typing import List, Set, Tuple


class Graph:
    def __init__(self, arr: List[List[int]]) -> None:
        self.graph = defaultdict(list)
        for a, b in arr:
            self.graph[a].append(b)
            self.graph[b].append(a)

    def search(self, root: int, visited: List[int]) -> List[int]:
        for path in self.graph[root]:
            if path not in visited:
                visited = self.search(path, visited + [path])
        return visited


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        ans: List[List[int]] = []

        for i in range(n):
            con = connections[:i] + connections[i + 1 :]
            graph = Graph(con)
            res = graph.search(connections[0][0], [])
            if len(res) != n:
                ans.append(connections[i])
                break
        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, List[List[int]], List[List[int]]]] = [
        (4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]]),
        (2, [[0, 1]], [[0, 1]]),
    ]

    def test_solution(self):
        for n, connections, expected in self.data:
            self.assertEqual(self.s.criticalConnections(n, connections), expected)


if __name__ == "__main__":
    main()
