from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i == 0:
                continue
            nums[i] = nums[i - 1] + nums[i]
        return nums


if __name__ == "__main__":
    s = Solution()
    s.runningSum([1, 2, 3, 4])
