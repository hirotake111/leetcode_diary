from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a = bin(n)[2:]
        return a[0] == "1" and len(a) % 2 == 1 and a[1:] == "0" * (len(a) - 1)

        # if n == 1:
        # return True
        # if n <= 3:
        # return False
        # while 0 < n:
        # if n % 2 == 1:
        # break
        # n >>= 1
        # if n % 2 == 1:
        # break
        # n >>= 1
        # if n == 1:
        # return True
        # return False


class Test(TestCase):
    data: List[Tuple[int, bool]] = [(16, True), (5, False), (1, True), (2, False)]

    def test_solution(self):
        s = Solution()
        for n, expected in self.data:
            self.assertEqual(s.isPowerOfFour(n), expected)


if __name__ == "__main__":
    main()
