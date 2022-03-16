from typing import List
from unittest import main, TestCase

"""
abcdedf
ccbcdffff
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = None
        for s in strs:
            if string == None:
                string = s
                continue
            tmp = ""
            for x, y in zip(string, s):
                if x == y:
                    tmp += x
                else:
                    break
            string = tmp

        return string


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(self.s.longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(self.s.longestCommonPrefix(["cir", "car"]), "c")


if __name__ == "__main__":
    main()
    # s = Solution()
    # assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    # assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    # assert s.longestCommonPrefix(["cir", "car"]) == ""
