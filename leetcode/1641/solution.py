"""
https://leetcode.com/problems/count-sorted-vowel-strings/
1641. Count Sorted Vowel Strings
"""
from unittest import TestCase, main
from typing import List, Tuple

"""
a, e, i, o, u

aa, ae, ai ,ao, au,
ee, ei, eo, eu
ii, io, iu
oo, ou,
uu

aaa, aae, aai, aao, aau
aee, aei, aeo, aeu
aii, aio, aiu
aoo, aou
auu

eee, eei, eeo, eeu
eii, eio, eiu
eoo, eou
euu

iii, iio, iiu
ioo, iou
iuu

ooo, oou
ouu

uuu
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = [1, 1, 1, 1, 1]
        for _ in range(n - 1):
            for i in range(5):
                if i > 0:
                    ans[i] = ans[i] + ans[i - 1]
        return sum(ans)


class TestSolution(TestCase):
    s = Solution()
    data: List[Tuple[int, int]] = [(1, 5), (2, 15), (33, 66045)]

    def test_solution(self):
        for n, expected in self.data:
            self.assertEqual(self.s.countVowelStrings(n), expected)


if __name__ == "__main__":
    main()
