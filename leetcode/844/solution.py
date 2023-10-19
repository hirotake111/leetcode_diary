"""
https://leetcode.com/problems/backspace-string-compare/
844. Backspace String Compare
"""
from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return func(s) == func(t)


def func(s: str) -> List[str]:
    stack = []
    for c in s:
        if c != "#":
            stack.append(c)
        elif len(stack):
            stack.pop()

    return stack
