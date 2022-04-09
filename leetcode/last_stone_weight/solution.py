from unittest import main, TestCase
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def func(stones: List[int]) -> int:
            l = len(stones)
            if l == 0:
                return 0
            if l == 1:
                return stones[0]
            return func(stones[: l - 2] + [abs(stones[-1] - stones[-2])])

        return func(sorted(stones))


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(self.s.lastStoneWeight([1]), 1)


if __name__ == "__main__":
    main()
