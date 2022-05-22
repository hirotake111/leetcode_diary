from unittest import TestCase, main
from typing import List, Set, Tuple


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        ans: List[List[int]] = []
        nodes: Set[int] = set()


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
