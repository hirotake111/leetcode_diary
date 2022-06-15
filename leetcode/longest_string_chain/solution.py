from functools import reduce
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d: Dict[str, int] = {}
        longest = 1

        for w in words:
            d[w] = 1

        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1 :]
                if prev_word in d:
                    d[word] = max(d[word], d[prev_word] + 1)
            longest = max(longest, d[word])

        return longest


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], int]] = [
        (["bdca", "bda", "ca", "dca", "a"], 4),
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.longestStrChain(input), expected)


if __name__ == "__main__":
    main()
