from unittest import main, TestCase

"""
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack:
                return False
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            elif c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False

        return False if stack else True
