from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [[-1, -1] for _ in s]

        def func1(idx: int) -> int:
            if not idx < n:
                return 1

            if s[idx] == "0":
                memo[idx][0] = 0
                return memo[idx][0]

            if memo[idx][0] != -1:
                return memo[idx][0]

            memo[idx][0] = func1(idx + 1) + func2(idx + 1)
            return memo[idx][0]

        def func2(idx: int) -> int:
            if n - 1 <= idx:
                # cannot make 2 digits
                return 0

            # at this point we are sure we can make 2 digits number using idx
            if s[idx] == "0":
                # invalid
                memo[idx][1] = 0
                return memo[idx][1]

            total = int(s[idx]) * 10 + int(s[idx + 1])
            if 26 < total:
                # total is too big
                memo[idx][1] = 0
                return memo[idx][1]

            # now we successfully created 2 digits number
            if idx == n - 2:
                memo[idx][1] = 1
                return memo[idx][1]

            memo[idx][1] = func1(idx + 2) + func2(idx + 2)
            return memo[idx][1]

        return func1(0) + func2(0)


class Test(TestCase):
    data_set: List[Tuple[str, int]] = [
        ("111111111111111111111111111111111111111111111", 1836311903),
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data_set:
            self.assertEqual(s.numDecodings(input), expected)


if __name__ == "__main__":
    main()
