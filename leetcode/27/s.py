"""
https://leetcode.com/problems/remove-element/
27. Remove Element
"""
from unittest import main, TestCase
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1, l = 0, len(nums)
        for i in range(l):
            if nums[i] == val:
                continue
            nums[p1] = nums[i]
            p1 += 1
        return p1


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        _ = None
        nums = [3, 2, 2, 3]
        val = 3
        expected = [2, 2, _, _]
        k = self.s.removeElement(nums, val)
        self.assertEqual(nums[:k], expected[:k])
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 1, 3, 0, 4, _, _, _]
        k = self.s.removeElement(nums, val)
        self.assertEqual(nums[:k], expected[:k])


if __name__ == "__main__":
    main()
