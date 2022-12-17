"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        operator = ("+", "-", "*", "/")

        for t in tokens:
            if t not in operator:
                # t is a number -> push it to the stack
                stack.append(int(t))
                continue
            # pick up two numbers from  the stack
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                sign = 1
                if a < 0:
                    a, sign = -a, -1
                if b < 0:
                    b, sign = -b, sign * -1
                stack.append(a // b * sign)

        return stack[0]


class Test(TestCase):
    data: List[Tuple[List[str], int]] = [
        # (["2", "1", "+", "3", "*"], 9),
        # (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.evalRPN(input), expected)


if __name__ == "__main__":
    main()
