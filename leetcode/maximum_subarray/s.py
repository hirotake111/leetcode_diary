from typing import List
from unittest import main, TestCase


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current, ans = 0, max(nums)
        for i in range(len(nums)):
            current += nums[i]
            if current > ans:
                ans = current
            if current < 0:
                # reset current value as it does not contribute the subarray
                current = 0
        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        self.assertEqual(self.s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.s.maxSubArray([1]), 1)
        self.assertEqual(self.s.maxSubArray([5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    main()
