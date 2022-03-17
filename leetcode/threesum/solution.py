from typing import List
from unittest import main, TestCase


def func(start: int, end: int, nums: List[int]) -> List[int]:
    target = -(nums[end] + nums[start])
    if target in nums[start + 1 : end]:
        return [nums[start], target, nums[end]]


def f(sorted: List[int], result: List[List[int]]) -> List[List[int]]:
    # edge cases
    if len(sorted) < 3:
        return result
    if sorted[0] > 0 or sorted[-1] < 0:
        return result

    lowest = sorted[0]
    highest = sorted[-1]
    mid = -(lowest + highest)
    shrinked_arr = sorted[1:-1]
    if mid in shrinked_arr and [lowest, mid, highest] not in result:
        # bingo
        result.append([lowest, mid, highest])

    if abs(lowest) == highest:
        # return f(sorted[1:], f(sorted[:-1], result))
        return f(sorted[1:], f(sorted[:-1], result))
    elif abs(lowest) > highest:
        # increment lowest index
        return f(sorted[1:], result)
    # decrement highest index
    return f(sorted[:-1], result)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return f(nums, [])


class TestSolution(TestCase):
    s = Solution()

    def test_solutio(self):
        # self.assertEqual(
        #     self.s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        # )
        # self.assertEqual(self.s.threeSum([]), [])
        # self.assertEqual(self.s.threeSum([0]), [])
        # self.assertEqual(self.s.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(
            self.s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]),
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        )
        # self.assertEqual(
        #     self.s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]),
        #     [
        #         [-4, 0, 4],
        #         [-4, 1, 3],
        #         [-3, -1, 4],
        #         [-3, 0, 3],
        #         [-3, 1, 2],
        #         [-2, -1, 3],
        #         [-2, 0, 2],
        #         [-1, -1, 2],
        #         [-1, 0, 1],
        #     ],
        # )


if __name__ == "__main__":
    main()
