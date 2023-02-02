"""
https://leetcode.com/problems/verifying-an-alien-dictionary/
953. Verifying an Alien Dictionary
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}

        def validate(s1: str, s2: str) -> bool:
            for c1, c2 in zip(s1, s2):
                # If two characters are identical, move to the next
                if d[c1] == d[c2]:
                    continue
                # Otherwise, c1 should be smaller number
                return d[c1] < d[c2]
            # If we reaches this line, two words are the same within the length of min(len(s1), len(s2)).
            # In this case, len(s1) must be smaller than len(s2)
            return len(s1) <= len(s2)

        for i in range(len(words) - 1):
            # If validation is failed, return False
            if not validate(words[i], words[i + 1]):
                return False
        # All validations were success -> return True
        return True
