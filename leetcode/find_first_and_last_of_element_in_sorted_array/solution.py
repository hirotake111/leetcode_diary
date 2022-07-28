from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_index(left: int, right: int) -> int:
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] == target:
                    return middle
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1

        def spread(i: int) -> List[int]:
            left = right = i
            has_changed = True
            while has_changed:
                has_changed = False
                if 0 < left and nums[left - 1] == target:
                    left -= 1
                    has_changed = True
                if right < length - 1 and nums[right + 1] == target:
                    right += 1
                    has_changed = True
            return [left, right]

        length = len(nums)
        if length == 0:
            return [-1, -1]

        return spread(search_index(0, length - 1))


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, List[int]]] = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([1, 2, 3], 3, [2, 2]),
        ([1, 5], 4, [-1, -1]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ]

    def test_solution(self):
        for nums, target, expected in self.data:
            self.assertEqual(self.s.searchRange(nums, target), expected)


if __name__ == "__main__":
    main()
