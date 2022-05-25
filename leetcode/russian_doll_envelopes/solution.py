# https://leetcode.com/problems/russian-doll-envelopes/
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def func(arr: List[List[int]]) -> int:
            cw, ch = 0, 0
            ans = 0
            for w, h in arr:
                if cw < w and ch < h:
                    ans += 1
                    cw, ch = w, h
            return ans

        return max(func(sorted(envelopes)), func(sorted(envelopes, key=lambda x: x[1])))
        # if l == 0:
        #     return 0
        # if l == 1:
        #     return 1

        # envelopes.sort()
        # envelopes.append([100001, 100001])

        # while next < l:
        #     if next >= l or envelopes[i][0] != envelopes[next][0]:
        #         i, next = i + 1, next + 1
        #         ans += 1
        #         continue
        #     # i == next
        #     while next < l and envelopes[i][0] == envelopes[next][0]:
        #         i, next = i + 1, next + 1

        # return ans + 1


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int]] = [
        (
            [
                [2, 100],
                [3, 200],
                [4, 300],
                [5, 500],
                [5, 400],
                [5, 250],
                [6, 370],
                [6, 360],
                [7, 380],
            ],
            5,
        ),
        ([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]], 3),
        ([[4, 5], [6, 7], [2, 3]], 3),
        ([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]], 4),
        ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
        ([[1, 1], [1, 1], [1, 1]], 1),
    ]

    def test_solution(self):
        for envelopes, expected in self.data:
            self.assertEqual(self.s.maxEnvelopes(envelopes), expected)


if __name__ == "__main__":
    main()
