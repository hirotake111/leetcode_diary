from typing import List

"""
abcdedf
ccbcdffff
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        length = len(strs)
        if len(strs) == 1:
            return strs[0]
        if len()


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    # assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
