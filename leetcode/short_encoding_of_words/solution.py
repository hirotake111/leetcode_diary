from re import sub
from typing import Dict, List, Set, Tuple, Optional
from typing_extensions import Self
from unittest import TestCase, main


class Trie:
    ch: str
    next: Optional["Trie"]

    def __init__(self, word: str) -> None:
        ch = word[0]
        rest = word[1:]
        self.ch = ch
        if len(rest) > 0:
            self.next = Trie(word=rest)
        else:
            self.next = None


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        seen: Set[str] = set()
        ans = 0
        words.sort(key=len)

        for w in words:
            l = len(w)
            for i in range(l):
                substring = w[l - i - 1 :]
                if substring in seen:
                    seen.remove(substring)
                    ans -= i + 2
                    break

            ans += l + 1
            seen.add(w)

        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], int]] = [
        (["time", "time", "time", "time"], 5),
        (["time", "me", "bell"], 10),
        (["t"], 2),
    ]

    def test_solution(self):
        for words, expected in self.data:
            self.assertEqual(self.s.minimumLengthEncoding(words=words), expected)


if __name__ == "__main__":
    main()
