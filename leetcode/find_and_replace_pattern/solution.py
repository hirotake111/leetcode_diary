from re import I, L
from tkinter import W
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1 and p not in m2:
                    m1[w] = p
                    m2[p] = w
                    continue
                if w in m1 and p in m2 and m1[w] == p and m2[p] == w:
                    continue
                return False
            return True

        return list(filter(match, words))


#         l = len(pattern)
# target = self.str_to_int(pattern)
# answer: List[str] = []

# for arr in words:
# if len(arr) != l:
# continue
# if self.str_to_int(arr) == target:
# answer.append(arr)

# return answer

# def str_to_int(self, arr: str) -> List[int]:
# l = len(arr)
# d: Dict[str, int] = {}
# pattern_int: List[int] = [0] * l
# count = 0
# for i, n in enumerate(arr):
# result = d.get(n)
# if result is None:
# pattern_int[i] = count
# d[n] = count
# count += 1
# else:
# pattern_int[i] = result
# return pattern_int


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], str, List[str]]] = [
        (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),
        (["a", "b", "c"], "a", ["a", "b", "c"]),
    ]

    def test_solution(self):
        for words, pattern, expected in self.data:
            self.assertEqual(self.s.findAndReplacePattern(words, pattern), expected)


if __name__ == "__main__":
    main()
