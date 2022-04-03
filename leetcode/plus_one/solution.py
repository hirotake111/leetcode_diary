from typing import List
from unittest import main, TestCase


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # total = 0

        # for i in digits:
        #     total = total * 10 + i

        # return [int(c) for c in str(total + 1)]
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < 10:
                break
            digits[i] = 0
            digits[i - 1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # self.assertEqual(self.s.plusOne([1, 2, 3]), [1, 2, 4])
        # self.assertEqual(self.s.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        # self.assertEqual(self.s.plusOne([9]), [1, 0])
        self.assertEqual(self.s.plusOne([9, 9]), [1, 0, 0])


if __name__ == "__main__":
    main()
