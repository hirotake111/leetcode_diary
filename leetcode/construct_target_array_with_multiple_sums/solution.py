from audioop import reverse
from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        target.sort(reverse=True)
        summary = sum(target)
        l = len(target)

        if l == 0:
            return False

        if l == 1:
            return True if target[0] == 1 else False

        if l == 2:
            if target[0] % target[1] == 0 and target[1] != 1:
                return False
            return True

        while True:
            n = target[0]
            summary -= n
            if n <= summary:
                return False

            n %= summary

            if n == 1:
                target = target[1:] + [1]
                summary += 1
                if target == [1] * l:
                    return True
            else:
                target[0] = n
                target.sort(reverse=True)
                summary += n


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], bool]] = [
        ([8, 5], True),
        ([2, 900000002], False),
        ([1, 1, 999999999], True),
        ([1, 1000000000], True),
        ([9, 3, 5], True),
        ([1, 1, 1, 2], False),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.isPossible(input), expected)


if __name__ == "__main__":
    main()
