"""
https://leetcode.com/problems/optimal-partition-of-string/
2405. Optimal Partition of String

Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
"""
from typing import Set


class Solution:
    def partitionString(self, s: str) -> int:
        unique: Set[str] = set()
        answer = 0

        for c in s:
            if c in unique:
                # The character is not unique anymore within the current substring
                # -> increment answer and clear the hash set
                answer += 1
                unique.clear()
            unique.add(c)

        # If the hash set has any elements in it,
        # Add 1 to the answer (as there is another unique substring)
        return answer + 1 if len(unique) else answer
