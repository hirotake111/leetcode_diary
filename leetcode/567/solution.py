"""
https://leetcode.com/problems/permutation-in-string/
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Sliding window approach"""
        if len(s2) < len(s1):
            return False

        # Populate frequency of s1 and s2
        arr1, arr2 = [0] * 26, [0] * 26
        for i, c1 in enumerate(s1):
            arr1[ord(c1) - 97] += 1
            c2 = s2[i]
            arr2[ord(c2) - 97] += 1

        if arr1 == arr2:
            return True

        for oldIdx in range(len(s2) - len(s1)):
            newIdx = oldIdx + len(s1)
            c_old = s2[oldIdx]
            c_new = s2[newIdx]
            # Decrement value for earlier character, increment value for new character
            arr2[ord(c_old) - 97] -= 1
            arr2[ord(c_new) - 97] += 1
            # compare it
            if arr1 == arr2:
                return True
        return False


class Test(TestCase):
    data: List[Tuple[str, str, bool]] = [
        ("ab", "eidbaooo", True),
    ]

    def test_solution(self):
        solution = Solution()
        for a, b, c in self.data:
            self.assertEqual(solution.checkInclusion(a, b), c)


if __name__ == "__main__":
    main()
