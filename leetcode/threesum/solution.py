from typing import List
from unittest import main, TestCase


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        result = []

        # while l > idx1 + 2:
        for idx1 in range(l):
            # if nums[idx1] == nums[idx1-1], we have already tried it -> skip it
            if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
                continue

            idx2 = idx1 + 1
            idx3 = l - 1
            while idx2 < idx3:
                s = nums[idx1] + nums[idx2] + nums[idx3]
                # validate total value
                if s == 0:
                    result.append([nums[idx1], nums[idx2], nums[idx3]])
                if s < 0:
                    # this should be the lowest value at this point
                    # -> we cannot decrease the total value anymore
                    # -> increase idx2
                    prev = nums[idx2]
                    while idx2 < l and nums[idx2] == prev:
                        idx2 += 1
                elif s >= 0:
                    # this sould be the highest value at this point
                    # -> we cannot increase the total value anymore
                    # -> decrease idx3
                    prev = nums[idx3]
                    while idx3 > 0 and nums[idx3] == prev:
                        idx3 -= 1

        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(
            self.s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )
        self.assertEqual(self.s.threeSum([]), [])
        self.assertEqual(self.s.threeSum([0]), [])
        self.assertEqual(self.s.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(
            self.s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]),
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        )
        self.assertEqual(
            self.s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]),
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        )


if __name__ == "__main__":
    main()
