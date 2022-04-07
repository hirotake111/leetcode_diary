from unittest import main, TestCase
from typing import List

"""
Given an integer array arr, and an integer target, 
return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
Constraints:
3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr = list(filter(lambda x: x >= target, sorted(arr)))
        l = len(arr)
        ans = 0

        def func(summary: int, idx: int):
            for i in range(idx, l):
                tmp = summary + arr[i]
                if tmp == target:
                    ans += 1

        func(0, 0)

        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        target = 8
        expected = 20
        self.assertEqual(self.s.threeSumMulti(arr, target), expected)
        arr = [1, 1, 2, 2, 2, 2]
        target = 5
        expected = 12
        self.assertEqual(self.s.threeSumMulti(arr, target), expected)


if __name__ == "__main__":
    main()
