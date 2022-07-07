from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        memo = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        self.answer = False

        if l1 + l2 != l3:
            return False

        def func(i1: int, i2: int, i3: int):
            if self.answer == True or memo[i1][i2] == 1:
                return

            if i1 == l1 and i2 == l2 and i3 == l3:
                self.answer = True
                return

            if i1 == l1:
                self.answer = s2[i2:] == s3[i3:]
                memo[i1][i2] = 1
                return

            if i2 == l2:
                self.answer = s1[i1:] == s3[i3:]
                memo[i1][i2] = 1
                return

            if s1[i1] == s3[i3]:
                func(i1 + 1, i2, i3 + 1)
            if s2[i2] == s3[i3]:
                func(i1, i2 + 1, i3 + 1)

            memo[i1][i2] = 1

        func(0, 0, 0)
        return self.answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, str, str, bool]] = [
        ("aabaac", "aadaaeaaf", "aadaaeaabaafaac", True),
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ]

    def test_solution(self):
        for s1, s2, s3, expected in self.data:
            self.assertEqual(self.s.isInterleave(s1, s2, s3), expected)


if __name__ == "__main__":
    main()
