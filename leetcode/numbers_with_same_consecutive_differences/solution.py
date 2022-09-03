from itertools import combinations
from queue import Queue
from typing import List, Set, Tuple
from unittest import TestCase, main


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """dfs approach"""
        answer: Set[int] = set()
        queue: Queue[Tuple[int, int]] = Queue()
        for i in range(1, 10):
            queue.put((i, i))

        while not queue.empty():
            total, i = queue.get()
            for a in (i - k, i + k):
                if not (0 <= a < 10):
                    continue
                new_total = total * 10 + a
                if 10 ** (n - 1) <= new_total:
                    answer.add(new_total)
                else:
                    queue.put((new_total, a))

        return list(answer)

        # """bfs approach"""
        # answer: Set[int] = set()

        # def dfs(num: int, i: int):
        #     for j in (k, -k):
        #         if 0 <= i + j < 10:
        #             next_val = num * 10 + i + j
        #             if 10 ** (n - 1) <= next_val:
        #                 answer.add(next_val)
        #             else:
        #                 dfs(next_val, i + j)

        # for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        #     dfs(i, i)
        # return list(answer)


class Test(TestCase):
    data: List[Tuple[int, int, List[int]]] = [
        # (3, 7, [181, 292, 707, 818, 929]),
        (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
        (2, 0, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
    ]

    def test_solution(self):
        s = Solution()
        for n, k, expected in self.data:
            self.assertEqual(sorted(s.numsSameConsecDiff(n, k)), expected)


if __name__ == "__main__":
    main()
