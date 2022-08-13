from collections import Counter
from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length, s_length = len(words[0]), len(s)
        word_counts = Counter(words)
        answer: List[int] = []

        def func(idx: int):
            word = s[idx : idx + word_length]
            if word not in word_counts:
                return False
            counts = word_counts.copy()
            while True:
                if word not in counts or counts[word] == 0:
                    break
                counts[word] -= 1
                idx += word_length
                word = s[idx : idx + word_length]
            if sum(counts.values()) == 0:
                return True
            return False

        for i in range(0, s_length - word_length + 1):
            if func(i):
                answer.append(i)

        return answer


class Test(TestCase):
    data: List[Tuple[str, List[str], List[int]]] = [
        ("a", ["a"], [0]),
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ]

    def test_solution(self):
        solution = Solution()
        for s, words, expected in self.data:
            self.assertEqual(solution.findSubstring(s, words), expected)


if __name__ == "__main__":
    main()
