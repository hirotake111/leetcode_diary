from typing import List, Tuple
from unittest import main, TestCase


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: List[str] = []
        current: str = ""
        for ch in s:
            l = len(current)
            # this only happens very fist time
            if l == 0:
                current = ch
                continue

            if current[0] != ch:
                # push current to stack
                stack.append(current)
                current = ch
                continue

            # now we can say current == ch
            if l + 1 == k:
                # we found k-adjacent duplicates
                if len(stack) > 0:
                    # pop the last elm in stack and make it current
                    current = stack.pop()
                else:
                    # no elm in stack - just empty current value
                    current = ""
                continue

            # current + ch is duplicates, but the length does not reach k - just concatenate them
            current += ch

        stack.append(current)
        return "".join(stack)


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        data: List[Tuple[str, int, str]] = [
            ("abcd", 2, "abcd"),
            ("deeedbbcccbdaa", 3, "aa"),
            ("pbbcggttciiippooaais", 2, "ps"),
        ]
        for s, k, expected in data:
            output = self.s.removeDuplicates(s, k)
            self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
