"""
https://leetcode.com/problems/merge-strings-alternately/
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        l1 = len(word1)
        l2 = len(word2)
        j = max(l1, l2)
        k = 0
        answer = [""] * (l1 + l2)

        while i < j:
            if i < l1:
                answer[k] = word1[i]
                k += 1
            if i < l2:
                answer[k] = word2[i]
                k += 1
            i += 1

        return "".join(answer)
