from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        l = len(words)
        # generate a list of bit map
        arr: List[int] = [0] * l
        for i, word in enumerate(words):
            for letter in word:
                arr[i] = arr[i] | 1 << (ord(letter) - 97)
        for j in range(l):
            for k in range(l):
                if arr[j] & arr[k] == 0:  # these do not share common letters
                    ans = max(ans, len(words[j] * len(words[k])))
        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], int]] = [
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
        (["a", "aa", "aaa", "aaaa"], 0),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.maxProduct(input), expected)


if __name__ == "__main__":
    main()
