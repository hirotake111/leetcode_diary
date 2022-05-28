from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num > 0:
            if num % 2 == 1:
                num -= 1
            else:
                num //= 2
            ans += 1

        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int]] = [(14, 6), (8, 4), (123, 12)]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.numberOfSteps(input), expected)


if __name__ == "__main__":
    main()
