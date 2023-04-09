from itertools import accumulate
from unittest import TestCase, main
from typing import List, Optional, Set, Tuple


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list: List[int] = list(accumulate(nums, min))
        s3s: list[int] = []
        l = len(nums)

        for i in range(l - 1, -1, -1):
            s1 = min_list[i]
            s2 = nums[i]
            if s2 <= s1:
                continue
            # s1 < s2
            # find s3 which is greater than s1
            while s3s and s3s[-1] <= s1:
                s3s.pop()
            # now we have s3 which is greater than s1, or no element in s3s
            if s3s and s3s[-1] < s2:
                return True
            s3s.append(s2)
        return False


class TestSolution(TestCase):
    s = Solution()
    data: List[Tuple[List[int], bool]] = [
        ([2, 3, 1, 2], False),
        # ([10, 12, 6, 8, 3, 11], True),
        # ([-2, 1, 1, -2, 1, 1], False),
        # ([1, 3, 2, 4, 5, 6, 7, 8, 9, 10], True),
        # ([1, 2, 3, 4, -4, -3, -5, -1], False),
        # ([3, 5, 0, 3, 4], True),
        # ([1, 2, 3, 4], False),
        ([3, 1, 4, 2], True),
        # ([-1, 3, 2, 0], True),
    ]

    def test_solution(self):
        for nums, expected in self.data:
            self.assertEqual(self.s.find132pattern(nums=nums), expected)


if __name__ == "__main__":
    main()
