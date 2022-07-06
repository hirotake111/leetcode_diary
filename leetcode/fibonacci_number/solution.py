from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        memo = [-1] * (n + 1)
        memo[0], memo[1] = 0, 1

        def func(n):
            if memo[n] != -1:
                return memo[n]
            return func(n - 1) + func(n - 2)

        return func(n)
        """
        a, b = 0, 1
        
        for _ in range(n):
            a, b = b, a+b
        return a
        """


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int]] = [(2, 1), (3, 2), (4, 3)]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.fib(input), expected)


if __name__ == "__main__":
    main()
