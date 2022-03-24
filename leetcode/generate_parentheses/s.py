from unittest import main, TestCase
from typing import List


"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        s = []

        def backtrack(opn=0, clse=0):
            if len(s) == 2 * n:
                # now we can say s is valid pair -> add it to result
                return result.append("".join(s))
            if n > opn:
                # we can add "("
                s.append("(")
                # then invoke backtrack() recursively
                backtrack(opn + 1, clse)
                # pop out one "(" and continue
                s.pop()
            if opn > clse:
                # we can still add closing bracket
                s.append(")")
                # the ninvoke backtrack() recursively
                backtrack(opn, clse + 1)
                s.pop()
            # (if opn < clse, then it's not valid one, and in that case we can just igonre it)

        backtrack()
        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(
            self.s.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        self.assertEqual(self.s.generateParenthesis(1), ["()"])


if __name__ == "__main__":
    main()
