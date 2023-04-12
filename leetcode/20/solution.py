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
        m = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in [")", "}", "]"]:
                if len(stack) == 0 or stack[-1] != m[c]:
                    return False
                stack.pop()
                continue
            stack.append(c)

        return True if len(stack) == 0 else False


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.isValid(s="()"), True)
        self.assertEqual(self.s.isValid(s="()[]{}"), True)
        self.assertEqual(self.s.isValid(s="(]"), False)


if __name__ == "__main__":
    main()
