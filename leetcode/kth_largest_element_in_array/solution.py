from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int]] = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    def test_solution(self):
        for nums, k, expected in self.data:
            self.assertEqual(self.s.findKthLargest(nums, k), expected)


if __name__ == "__main__":
    main()
