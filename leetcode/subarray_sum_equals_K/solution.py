from collections import Counter
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer, l = 0, len(nums)
        counter: Counter[int] = Counter({0: 1})  # key: prefix sum

        if l == 0:
            return 0
        if l == 1:
            return 1 if nums[0] == k else 0

        prefix_sum = 0
        for i in range(l):
            prefix_sum += nums[i]
            answer += counter[prefix_sum - k]
            counter[prefix_sum] += 1

        return answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int]] = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
    ]

    def test_solution(self):
        for nums, k, expected in self.data:
            self.assertEqual(self.s.subarraySum(nums, k), expected)


if __name__ == "__main__":
    main()
