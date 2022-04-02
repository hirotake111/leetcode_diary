from typing import List
from unittest import main, TestCase


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = high // 2

        while low <= high:
            if nums[mid] == target:
                return mid
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
            if (
                nums[mid] < target < nums[high]
                or target < nums[high] < nums[mid]
                or nums[low] < nums[mid] < target
            ):
                low = mid + 1
            else:
                high = mid - 1
            mid = low + (high - low) // 2
        return -1


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        self.assertEqual(self.s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0), 4)
        self.assertEqual(self.s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3), -1)


if __name__ == "__main__":
    main()
