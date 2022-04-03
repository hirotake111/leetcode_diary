from unittest import main, TestCase
from typing import Any, List, Union


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        O(n) approach
        """
        # arr: List[int] = []
        # while len(nums1) > 0 or len(nums2) > 0:
        #     if len(nums1) == 0:
        #         arr.append(nums2[0])
        #         nums2 = nums2[1:]
        #         continue
        #     if len(nums2) == 0:
        #         arr.append(nums1[0])
        #         nums1 = nums1[1:]
        #         continue
        #     if nums1[0] < nums2[0]:
        #         arr.append(nums1[0])
        #         nums1 = nums1[1:]
        #         continue
        #     arr.append(nums2[0])
        #     nums2 = nums2[1:]

        # l = len(arr)
        # if l % 2 == 1:
        #     return arr[l // 2]
        # return (arr[l // 2] + arr[l // 2 - 1]) / 2
        """
        O(log(n)) approach
        """

        def get_median(nums: List[int]) -> float:
            l = len(nums)
            if l % 2 == 0:
                # nums2 is even
                return (nums[l // 2] + nums[l // 2 - 1]) / 2
            # nums2 is odd
            return nums[l // 2]

        # calculate length of each array
        l1, l2 = len(nums1), len(nums2)
        inf = 1000001

        # if either of arrays has no elements, then return the median of the other
        if l1 == 0:
            return get_median(nums2)
        if l2 == 0:
            return get_median(nums1)

        # if we can concatenate 2 arrays, the result is much easier
        if nums1[0] > nums2[-1]:
            return get_median(nums2 + nums1)
        if nums2[0] > nums1[-1]:
            return get_median(nums1 + nums2)

        # concatenate -inf and inf
        nums1 = [-inf] + nums1 + [inf]
        nums2 = [-inf] + nums2 + [inf]
        l1 += 2
        l2 += 2
        l = l1 + l2

        # get initial medians
        if l1 >= l2:
            m2 = l2 // 2 - 1
            m1 = l // 2 - m2 - 2
        else:
            m1 = l1 // 2
            m2 = l // 2 - m1 - 2

        while True:
            if nums1[m1] <= nums2[m2 + 1] and nums2[m2] <= nums1[m1 + 1]:
                # found the medians
                break
            if nums1[m1] >= nums2[m2 + 1]:
                m2 += 1
                m1 -= 1
                continue
            m1 += 1
            m2 -= 1

        if l % 2 == 1:
            return min(nums1[m1 + 1], nums2[m2 + 1])
        # l is even
        return (max(nums1[m1], nums2[m2]) + min(nums1[m1 + 1], nums2[m2 + 1])) / 2


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]), 2.0)
        self.assertEqual(self.s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]), 2.5)
        self.assertEqual(
            self.s.findMedianSortedArrays([2], [1, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5
        )
        self.assertEqual(self.s.findMedianSortedArrays([1, 2, 4, 50, 60], [2, 3]), 3)


""""
[1,2,[4],50,60]
[  2,[3]]
[1,2,2,3,4,50,60]
"""

if __name__ == "__main__":
    main()
