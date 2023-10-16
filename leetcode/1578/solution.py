"""
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
1578. Minimum Time to Make Rope Colorful
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        # edge case
        if n < 1:
            return 0

        # at this point we are sure colors has at least 2 elements
        answer, prev, cur = 0, 0, 1

        while cur < n:
            max_time = neededTime[prev]
            while cur < n and colors[cur] == colors[prev]:
                max_time = max(max_time, neededTime[cur])
                cur += 1

            if cur != prev + 1:
                answer += sum(neededTime[prev:cur]) - max_time
                prev = cur - 1
            else:
                prev, cur = prev + 1, cur + 1

        return answer


class Test(TestCase):
    data_set: List[Tuple[str, List[int], int]] = [
        ("bbbaaa", [4, 9, 3, 8, 8, 9], 23),
        ("abaac", [1, 2, 3, 4, 5], 3),
        ("abc", [1, 2, 3], 0),
        ("aabaa", [1, 2, 3, 4, 1], 2),
    ]

    def test_solution(self):
        s = Solution()
        for colors, time, expected in self.data_set:
            self.assertEquals(s.minCost(colors, time), expected)


if __name__ == "__main__":
    main()
