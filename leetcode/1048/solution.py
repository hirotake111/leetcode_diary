"""
https://leetcode.com/problems/longest-string-chain/
1048. Longest String Chain
"""

from typing import List, Dict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d: Dict[str, int] = {}
        longest = 1

        for w in words:
            d[w] = 1

        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1 :]
                if prev_word in d:
                    d[word] = max(d[word], d[prev_word] + 1)
            longest = max(longest, d[word])

        return longest