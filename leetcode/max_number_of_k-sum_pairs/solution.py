from collections import Counter, defaultdict
from typing import DefaultDict, Dict, List, Tuple
from unittest import main, TestCase


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # ans = 0
        # d: DefaultDict[int, int] = defaultdict(int)
        # for i in nums:
        #     if k - i in d:
        #         if d[k - i] == 1:
        #             d.pop(k - i)
        #         else:
        #             d[k - i] -= 1
        #         ans += 1
        #     elif i < k:
        #         d[i] += 1
        # return ans
        ans = 0
        counts = Counter(nums)
        for key, v in counts.items():
            ans += min(counts[k - key], v)
        return ans // 2


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        data: List[Tuple[List[int], int, int]] = [
            ([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3, 4),
            ([1, 2, 3, 4], 5, 2),
            ([3, 1, 3, 4, 3], 6, 1),
        ]

        for nums, k, expected in data:
            self.assertEqual(self.s.maxOperations(nums, k), expected)


if __name__ == "__main__":
    main()
