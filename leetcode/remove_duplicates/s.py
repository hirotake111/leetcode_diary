from unittest import main, TestCase
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = sorted(list(set(nums)))
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        input = [1, 1, 2]
        expected = [1, 2, 2]
        k = self.s.removeDuplicates(input)
        self.assertEqual(input, expected)
        self.assertEqual(k, 2)
        input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        k = self.s.removeDuplicates(input)
        self.assertEqual(input, expected)
        self.assertEqual(k, 5)
        input = [-1, 0, 0, 0, 0, 3, 3]
        expected = [-1, 0, 3, 0, 0, 3, 3]
        k = self.s.removeDuplicates(input)
        self.assertEqual(input, expected)
        self.assertEqual(k, 3)


if __name__ == "__main__":
    main()
