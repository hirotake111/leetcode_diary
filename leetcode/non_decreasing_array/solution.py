from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = len(nums)
        flag = False
        highest = nums[0]

        if l < 3:
            return True

        if l == 3:
            return False if nums[0] > nums[1] > nums[2] else True

        for i in range(l - 1):
            if highest <= nums[i + 1]:
                highest = nums[i + 1]
                continue

            if flag == True:
                return False
            flag = True

            if i == 0 or nums[i - 1] <= nums[i + 1]:
                highest = nums[i + 1]
                continue

            highest = nums[i]

        return True


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], bool]] = [
        ([3, 4, 2, 3], False),
        ([4, 2, 3], True),
        ([4, 2, 1], False),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.checkPossibility(input), expected)


if __name__ == "__main__":
    main()
