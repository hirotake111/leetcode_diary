"""
https://leetcode.com/problems/sum-of-even-numbers-after-queries/
985. Sum of Even Numbers After Queries
"""
from typing import List, Tuple
from unittest import TestCase
from unittest.main import main


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        answer = [0] * len(queries)

        def is_even(num: int) -> bool:
            return not num & 1

        total = sum(v if is_even(v) else 0 for v in nums)

        for i, query in enumerate(queries):
            val, idx = query
            if is_even(nums[idx]):  # current value is even
                if is_even(val):  # val is also even and subtotal will be even too
                    total += val
                else:  # val is odd and subtotal will be odd
                    total -= nums[idx]
            else:  # current value is odd
                if is_even(val):  # val is even and subtotal will be odd
                    pass
                else:  # val and current value are both odd and subtoal will be even
                    total += nums[idx] + val

            nums[idx] += val
            answer[i] = total

        return answer


class Test(TestCase):
    data: List[Tuple[List[int], List[List[int]], List[int]]] = [
        ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
        ([1], [[4, 0]], [0]),
    ]

    def test_solution(self):
        s = Solution()
        for nums, queries, expected in self.data:
            self.assertEqual(s.sumEvenAfterQueries(nums, queries), expected)


if __name__ == "__main__":
    main()
