from typing import List, Tuple
from unittest import main, TestCase


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si, ti = len(s) - 1, len(t) - 1
        while si >= 0 or ti >= 0:
            sskip, tskip = 0, 0
            while si >= 0 and s[si] == "#":
                while s[si] == "#":
                    si -= 1
                    sskip += 1
                while sskip > 0:
                    si -= 1
                    sskip -= 1
                    if s[si] == "#" or si < 0:
                        break

            while ti >= 0 and t[ti] == "#":
                while t[ti] == "#":
                    ti -= 1
                    tskip += 1
                while tskip > 0:
                    ti -= 1
                    tskip -= 1
                    if t[ti] == "#" or ti < 0:
                        break

            if si < 0 and ti < 0:
                return True
            if si == -1 or ti == -1:
                return False
            if s[si] != t[ti]:
                return False

            si -= 1
            ti -= 1

        return True


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # s = "a#b#c#"
        # t = "c#d#"
        # self.assertEqual(self.s.backspaceCompare(s, t), True)
        s = "ab##"
        t = "c#d#"
        self.assertEqual(self.s.backspaceCompare(s, t), True)
        s = "ab#c"
        t = "ad#c"
        self.assertEqual(self.s.backspaceCompare(s, t), True)
        s = "a##c"
        t = "#a#c"
        self.assertEqual(self.s.backspaceCompare(s, t), True)


if __name__ == "__main__":
    main()
