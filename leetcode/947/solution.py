from typing import List, Tuple, Dict, DefaultDict
from collections import defaultdict
from unittest import TestCase, main


class Solution:
    removed = 0

    def removeStones(self, stones: List[List[int]]) -> int:
        # [0,1,2,3...]
        parent = [idx for idx in range(len(stones))]
        # [0,0,0...] this is used to compare two coordinates (higher wins)
        rank = [0] * len(stones)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            # get root of x and y
            root_x = find(x)
            root_y = find(y)
            # if they are already connected, skip it
            if root_x == root_y:
                return
            # compare rank between two (higher wins)
            if rank[root_y] < rank[root_x]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                # if rank for root x and y are the same,
                # root x wins and increment rank for root x
                parent[root_y] = root_x
                rank[root_x] += 1

            self.removed += 1

        def is_connected(a: List[int], b: List[int]) -> bool:
            return a[0] == b[0] or a[1] == b[1]

        # edge case
        if len(stones) == 1:
            return 0

        # union phase
        for i in range(len(stones) - 1):
            for j in range(i + 1, len(stones)):
                stone_a, stone_b = stones[i], stones[j]
                if is_connected(stone_a, stone_b):
                    union(i, j)

        return self.removed


class Test(TestCase):
    data_set: List[Tuple[List[List[int]], int]] = [
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
    ]

    def test_solution(self):
        for given, expected in self.data_set:
            s = Solution()
            self.assertEqual(s.removeStones(given), expected)


if __name__ == "__main__":
    main()
