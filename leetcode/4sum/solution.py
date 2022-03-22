from unittest import main, TestCase
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # sort the array first
        result = []
        l = len(nums)
        for idx1 in range(0, l - 3):
            if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
                # we have already tried it in the inner loop -> skip it
                continue

            for idx2 in range(idx1 + 1, l - 2):
                if idx2 > 1 and idx2 - 1 != idx1 and nums[idx2] == nums[idx2 - 1]:
                    # we have already tried it in the inner loop -> skip it
                    continue

                idx3 = idx2 + 1
                idx4 = l - 1
                while idx3 < idx4:
                    tmp = nums[idx1] + nums[idx2] + nums[idx3] + nums[idx4]
                    if tmp == target:
                        # add them to result
                        result.append([nums[idx1], nums[idx2], nums[idx3], nums[idx4]])
                    if tmp < target:
                        # we cannot decrease tmp -> increase idx3
                        while True:
                            idx3 += 1
                            if idx3 >= idx4 or nums[idx3] != nums[idx3 - 1]:
                                break
                        continue
                    # else, we cannot increase tmp -> decrease idx4
                    while True:
                        idx4 -= 1
                        if idx3 >= idx4 or nums[idx4] != nums[idx4 + 1]:
                            break

        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(
            self.s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        )
        self.assertEqual(self.s.fourSum(nums=[2, 2, 2, 2, 2], target=8), [[2, 2, 2, 2]])
        self.assertEqual(self.s.fourSum([0, 0, 0, 0], 1), [])
        self.assertEqual(
            self.s.fourSum([-2, -1, -1, 1, 1, 2, 2], 0),
            [[-2, -1, 1, 2], [-1, -1, 1, 1]],
        )
        """
        -2, -1,x
        -2, x,  -1
        --
        x, -1, -1,
        x, -1, -1, -1
        idx2 - 1 == idx1 and nums[idx1] == nums[idx2] -> do it
        idx2 - 1 != idx1 and nums[idx2 -1] == nums[idx2] -> skip it
        """


if __name__ == "__main__":
    main()
