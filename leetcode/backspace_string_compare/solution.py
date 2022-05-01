from typing import List, Tuple
from unittest import main, TestCase

"ab##"
"a#b#"
"a#b"
"ab#"


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            sskip, tskip = 0, 0
            while i >= 0 and (s[i] == "#" or sskip != 0):
                if s[i] == "#":
                    i -= 1
                    sskip += 1
                else:
                    i -= sskip
                    sskip = 0

            while j >= 0 and (t[j] == "#" or tskip != 0):
                if t[j] == "#":
                    j -= 1
                    tskip += 1
                else:
                    j -= tskip
                    tskip = 0

            if i < 0 or j < 0:
                return True
            if i == -1 or j == -1:
                return False
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1
        return True


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
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
