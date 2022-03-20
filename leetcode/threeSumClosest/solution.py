from unittest import main, TestCase
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # sort the array
        result = None  # value to be returned
        l = len(nums)

        for idx1 in range(l):  # 0 to l-1
            if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
                # in this case we have already tried those combination -> skip it
                continue

            idx2 = idx1 + 1
            idx3 = l - 1

            while idx2 < idx3:
                tmp = nums[idx1] + nums[idx2] + nums[idx3]
                # if tmp is closer to the target than current result, then update the result
                if result is None or abs(target - tmp) <= abs(target - result):
                    result = tmp

                if tmp == target:
                    # this should not be happen according to the description
                    return tmp

                if tmp > target:
                    # in this case we cannot increase tmp -> lower idx3
                    prev = nums[idx3]
                    while idx2 < idx3 and prev == nums[idx3]:
                        idx3 -= 1
                    continue

                # in this case we cannot decrease tmp -> upper idx2
                prev = nums[idx2]
                while idx2 < idx3 and prev == nums[idx2]:
                    idx2 += 1

        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(self.s.threeSumClosest([0, 0, 0], 1), 0)


if __name__ == "__main__":
    main()
