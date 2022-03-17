from unittest import main, TestCase


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}  # key: element, value: index of the array
        l = len(nums)
        if l < 2:
            return []

        if l == 2:
            return [0, 1]

        for i in range(l):
            v = m.get(target - nums[i])
            if v is not None:
                return [v, i]
            m[nums[i]] = i

        return []


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # self.assertEqual(self.s.twoSum([2, 7, 11, 15], 9), [0, 1])
        # self.assertEqual(self.s.twoSum(nums=[3, 2, 4], target=6), [1, 2])
        self.assertEqual(self.s.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    main()
