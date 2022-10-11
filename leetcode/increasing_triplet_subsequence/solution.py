from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = 2147483647
        # edge case
        if len(nums) <= 2:
            return False

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
