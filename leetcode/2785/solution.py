"""
https://leetcode.com/problems/sort-vowels-in-a-string/
2785. Sort Vowels in a String
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        copied = list(s)
        vowels = "AEIOUaeiou"
        vowels_only = [c for c in s if c in vowels]

        if len(vowels_only) == 0:
            return s

        vowels_only.sort()
        if len(vowels_only) == len(s):
            return "".join(vowels_only)

        i = 0
        for j, c in enumerate(s):
            if c in vowels:
                copied[j] = vowels_only[i]
                i += 1
        return "".join(copied)
