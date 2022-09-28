from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = list("L" + dominoes + "R")
        i, n = 0, len(d)

        while i < n - 1:
            while i < n - 1 and d[i + 1] != ".":
                i += 1
            j = i + 1

            if n - 1 <= i:
                break

            while d[j] == ".":
                j += 1

            if d[i] == "L" and d[j] == "L":
                # turn all "." to "L"
                while i < j:
                    d[i] = "L"
                    i += 1

            elif d[i] == "R" and d[j] == "L":
                a, b = i + 1, j - 1
                while a < b:
                    d[a], d[b] = "R", "L"
                    a, b = a + 1, b - 1

            elif d[i] == "R" and d[j] == "R":
                # turn them all to "R"
                while i < j:
                    d[i] = "R"
                    i += 1
            # d[i] == "L" and d[j] == "R" -> do nothing

            i = j

        return "".join(d[1 : n - 1])


class Test(TestCase):
    dataSet: List[Tuple[str, str]] = [
        # ("L...L..", "LLLLL.."),
        ("RR.L", "RR.L"),
        (".L.R...LR..L..", "LL.RR.LLRRLL.."),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.dataSet:
            self.assertEqual(s.pushDominoes(input), expected)


if __name__ == "__main__":
    main()
