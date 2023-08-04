"""
https://leetcode.com/problems/word-break/
139. Word Break
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] indicates whether (i - 1)th character is in the dict (true) or not
        # dp[0] is always true since it's the beginning of the string
        dp = [True] + [False] * len(s)
        words = set(wordDict)

        for i in range(len(s) + 1):
            for word in words:
                if len(word) <= i:
                    # begin points to the beginning of the substring
                    # Example:
                    # If word is "leet" and i is 4.
                    # Then begin = 4 - 4 = 0
                    begin = i - len(word)
                    sub_str = s[begin:i]
                    dp[i] |= sub_str == word and dp[begin]

        return dp[len(s)]
