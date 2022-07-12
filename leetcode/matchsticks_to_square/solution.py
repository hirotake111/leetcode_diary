from functools import cache
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total < 4:
            return False
        if total % 4 != 0:
            return False

        stick_length = total // 4
        arr_length = len(matchsticks)
        matchsticks.sort(reverse=True)

        @cache
        def dfs(l1: int, l2: int, l3: int, l4: int, i: int):
            # nonlocal stick_length
            # `nonlocal arr_length
            if l1 == l2 == l3 == l4 == stick_length:
                return True
            if i > arr_length:
                return False
            if max(l1, l2, l3, l4, stick_length) != stick_length:
                return False
            # sorting will speed up the process
            l1, l2, l3, l4 = sorted([l1, l2, l3, l4])
            return (
                dfs(l1 + matchsticks[i], l2, l3, l4, i + 1)
                or dfs(l1, l2 + matchsticks[i], l3, l4, i + 1)
                or dfs(l1, l2, l3 + matchsticks[i], l4, i + 1)
                or dfs(l1, l2, l3, l4 + matchsticks[i], i + 1)
            )

        return dfs(0, 0, 0, 0, 0)


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], bool]] = [
        ([1, 1, 2, 2, 2], True),
        ([3, 3, 3, 3, 4], False),
    ]

    def test_solution(self):
        pass


if __name__ == "__main__":
    main()
