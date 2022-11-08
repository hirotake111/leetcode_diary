from unittest import TestCase, main
from typing import List, Tuple


class Solution:
    def makeGood(self, s: str) -> str:
        m = {
            "a": "A",
            "b": "B",
            "c": "C",
            "d": "D",
            "e": "E",
            "f": "F",
            "g": "G",
            "h": "H",
            "i": "I",
            "j": "J",
            "k": "K",
            "l": "L",
            "m": "M",
            "n": "N",
            "o": "O",
            "p": "P",
            "q": "Q",
            "r": "R",
            "s": "S",
            "t": "T",
            "u": "U",
            "v": "V",
            "w": "W",
            "x": "X",
            "y": "Y",
            "z": "Z",
            "A": "a",
            "B": "b",
            "C": "c",
            "D": "d",
            "E": "e",
            "F": "f",
            "G": "g",
            "H": "h",
            "I": "i",
            "J": "j",
            "K": "k",
            "L": "l",
            "M": "m",
            "N": "n",
            "O": "o",
            "P": "p",
            "Q": "q",
            "R": "r",
            "S": "s",
            "T": "t",
            "U": "u",
            "V": "v",
            "W": "w",
            "X": "x",
            "Y": "y",
            "Z": "z",
        }
        stack: List[str] = []
        i = 0

        while i < len(s):
            if not stack:
                stack.append(s[i])
                i += 1
                continue

            if m[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1

        return "".join(stack)


class Test(TestCase):
    data_set: List[Tuple[str, str]] = [
        ("leEeetcode", "leetcode"),
        ("abBAcC", ""),
        ("s", "s"),
    ]

    def test_solution(self):
        s = Solution()
        for given, expected in self.data_set:
            self.assertEqual(s.makeGood(given), expected)


if __name__ == "__main__":
    main()
