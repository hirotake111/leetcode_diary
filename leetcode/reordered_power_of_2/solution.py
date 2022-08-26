from typing import List, Tuple
from unittest import TestCase, main
from itertools import permutations
from math import sqrt
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = Counter(str(n))
        m = 1
        while m < 1000000000:
            if target == Counter(str(m)):
                return True
            m <<= 1

        return False

        # if n == 1 or n == 4 or n == 8:
        #     return True
        # if n < 16:
        #     return False
        # s = str(n)
        # only_odd = True
        # for c in "24680":
        #     only_odd = only_odd and (c not in s)
        # if only_odd:
        #     return False

        # for candidate in permutations(str(n)):
        #     if candidate[0] == "0":
        #         continue
        #     if candidate[-1] in "13579":
        #         continue
        #     binary = bin(int("".join(candidate)))[2:]
        #     if binary[0] == "1" and binary[1:] == "0" * (len(binary) - 1):
        #         return True

        # return False


class Test(TestCase):
    data: List[Tuple[int, bool]] = [(218, True), (46, True), (1, True), (10, False)]

    def test_solution(self):
        s = Solution()
        for n, expected in self.data:
            self.assertEqual(s.reorderedPowerOf2(n), expected)


if __name__ == "__main__":
    main()
