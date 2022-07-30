from collections import Counter
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        c2: Dict[str, int] = {}
        for word in words2:
            sub_dict: Dict[str, int] = {}
            for ch in word:
                if ch in sub_dict:
                    sub_dict[ch] += 1
                else:
                    sub_dict[ch] = 1
            for k, v in sub_dict.items():
                if k not in c2 or c2[k] < v:
                    c2[k] = v

        def match(word: str) -> bool:
            c1 = Counter(word)
            for k, v in c2.items():
                if k not in c1 or c1[k] < v:
                    return False
            return True

        return list(filter(match, words1))


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], List[str], List[str]]] = [
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["lo", "eo"],
            ["google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "oo"],
            ["facebook", "google"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "o"],
            ["facebook", "google", "leetcode"],
        ),
    ]

    def test_solutio(self):
        for words1, words2, expected in self.data:
            self.assertEqual(self.s.wordSubsets(words1, words2), expected)


if __name__ == "__main__":
    main()
