from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr: List[int] = [1] * n
        for _ in range(m - 1):
            for i in range(n - 2, -1, -1):
                arr[i] += arr[i + 1]
        return arr[0]


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int, int]] = [(3, 7, 28), (3, 2, 3)]

    def test_solution(self):
        for m, n, expected in self.data:
            self.assertEqual(self.s.uniquePaths(m, n), expected)


if __name__ == "__main__":
    main()
