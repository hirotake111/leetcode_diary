from typing import List, Tuple
from unittest import main, TestCase


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """comparing sorted array approach"""
        # sorted_num, l = sorted(nums), len(nums)
        # i, j = 0, l - 1

        # if l == 1:
        #     return 0

        # while i < j:
        #     if nums[i] != sorted_num[i] and nums[j] != sorted_num[j]:
        #         break
        #     if nums[i] == sorted_num[i]:
        #         i += 1
        #     if nums[j] == sorted_num[j]:
        #         j -= 1

        # return 0 if i >= j else j - i + 1
        """two pointers approach"""
        length = len(nums)
        i, j = 0, length - 1

        if length < 2:
            return 0

        # determine the minimum index of left hand side
        while i + 1 < length:
            if nums[i] <= nums[i + 1]:
                i += 1
                continue

            k = i + 1
            while i >= 0 and nums[i] > nums[k]:
                i -= 1
            break

        if i == length - 1:
            return 0

        # determinethe minimum index of right hand side
        while j - 1 > i:
            if nums[j] >= nums[j - 1]:
                j -= 1
                continue
            k = j - 1
            while j < length and nums[j] < nums[k]:
                j += 1
            break

        return j - i - 1


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        data: Tuple[List[int], int] = [
            ([1, 3, 5, 4, 2], 4),
            ([5, 4, 3, 2, 1], 5),
            ([2, 1], 2),
            ([1, 2, 3, 3, 3], 0),
            ([2, 6, 4, 8, 10, 9, 15], 5),
            ([1, 2, 3, 4], 0),
            ([1], 0),
        ]
        for nums, expected in data:
            self.assertEqual(self.s.findUnsortedSubarray(nums), expected)


if __name__ == "__main__":
    main()
