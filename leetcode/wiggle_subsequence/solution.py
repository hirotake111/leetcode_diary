from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        prev_diff = 0  # 0:undefined, 1:up, 2:down
        delta_arr = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        for n in delta_arr:
            if n == 0:
                continue

            elif prev_diff == 0:  # undefined
                ans += 1
                prev_diff = 1 if n > 0 else 2

            elif prev_diff == 1:  # up
                if n < 0:
                    ans += 1
                    prev_diff = 2

            # prev is down
            elif n > 0:
                ans += 1
                prev_diff = 1

        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([1, 7, 4, 9, 2, 5], 6),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.wiggleMaxLength(input), expected)


if __name__ == "__main__":
    main()
