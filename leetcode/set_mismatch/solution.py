from tkinter import W
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        total_with_no_dup = sum(set(nums))
        total_expected = sum(range(1, len(nums) + 1))
        duplicated = total - total_with_no_dup
        missing = total_expected - total_with_no_dup

        return [duplicated, missing]
