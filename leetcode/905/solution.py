from typing import List
from unittest import main, TestCase


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2 == 1)
        # nums.sort(key=lambda x: x % 2 == 1)
        # return nums
        """intuitive approach"""
        # odd, even = [], []
        # for i in nums:
        #     if i % 2 == 0:
        #         even.append(i)
        #     else:
        #         odd.append(i)
        # return even + odd


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        data = [([3, 1, 2, 4], [2, 4, 3, 1]), ([0], [0])]
        for input, expected in data:
            self.assertEqual(self.s.sortArrayByParity(nums=input), expected)


if __name__ == "__main__":
    main()
