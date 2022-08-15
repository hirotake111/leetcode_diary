from collections import Counter
from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length, words_length, s_length = len(words[0]), len(words), len(s)
        word_counts = Counter(words)
        answer: List[int] = []

        def func(idx: int):
            sub = s[idx : idx + word_length]
            if sub not in word_counts:
                return False

            counts = word_counts.copy()
            words_used = 0
            while sub in counts and counts[sub] > 0:
                counts[sub] -= 1
                idx += word_length
                sub = s[idx : idx + word_length]
                words_used += 1

            return True if words_used == words_length else False

        for i in range(s_length - word_length + 1):
            if func(i):
                answer.append(i)

        return answer


class Test(TestCase):
    data: List[Tuple[str, List[str], List[int]]] = [
        (
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
            [13],
        ),
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
