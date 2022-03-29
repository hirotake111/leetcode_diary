from typing import List
from unittest import main, TestCase


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target, greater = None, None
        l = len(nums)
        if l < 2:
            return nums
        # find index i-1 that satisfies nums[i] > nums[i-1]
        for i in reversed(range(1, l)):
            if nums[i - 1] < nums[i]:  # swap it
                target, greater = i - 1, i
                break
        if target is None:
            # nums does not have a lexicographical larger rearrangement.
            nums.reverse()
            return
        # find index j that's just greater than i-1
        for j in range(target + 1, l):
            if nums[target] < nums[j] < nums[greater]:
                greater = j
        # swap those
        nums[target], nums[greater] = nums[greater], nums[target]
        # sort the rest
        nums[target + 1 :] = sorted(nums[target + 1 :])


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        a = [1, 2, 3]
        b = [1, 3, 2]
        self.s.nextPermutation(a)
        self.assertEqual(a, b)
        a = [3, 2, 1]
        b = [1, 2, 3]
        self.s.nextPermutation(a)
        self.assertEqual(a, b)
        a = [1, 1, 5]
        b = [1, 5, 1]
        self.s.nextPermutation(a)
        self.assertEqual(a, b)
        a = [1, 3, 2]
        b = [2, 1, 3]
        self.s.nextPermutation(a)
        self.assertEqual(a, b)


if __name__ == "__main__":
    main()
