from collections import defaultdict
from re import L
from typing import DefaultDict, Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        answer = [0] * l
        passed: DefaultDict[int, int] = defaultdict(int)
        for i in range(l - 1, -1, -1):
            current = nums[i]
            for k, v in passed.items():
                if k < current:
                    answer[i] += v
            passed[current] += 1
        return answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], List[int]]] = [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([-1], [0]),
        ([-1, -1], [0, 0]),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.countSmaller(input), expected)


if __name__ == "__main__":
    main()
