from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = [0] + nums1, [0] + nums2
        n1, n2 = len(nums1), len(nums2)
        dp: List[List[int]] = [[0] * n2 for _ in nums1]

        for i in range(1, n1):
            for j in range(1, n2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        return max([max(arr) for arr in dp])

        # if nums1 == nums2:
        # return len(nums1)
        # n1, n2 = len(nums1), len(nums2)
        # dp: List[List[int]] = [[0] * (n2 + 1) for _ in nums1 + [0]]
        # for i in range(n1 - 1, -1, -1):
        # for j in range(n2 - 1, -1, -1):
        # if nums1[i] == nums2[j]:
        # dp[i][j] = dp[i + 1][j + 1] + 1

        # return max([max(arr) for arr in dp])


class Test(TestCase):
    data: List[Tuple[List[int], List[int], int]] = [
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),
    ]

    def test_solution(self):
        s = Solution()
        for nums1, nums2, expected in self.data:
            self.assertEqual(s.findLength(nums1, nums2), expected)


if __name__ == "__main__":
    main()
