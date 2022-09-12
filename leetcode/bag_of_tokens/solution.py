from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        begin, end = 0, len(tokens) - 1
        score = 0

        while begin <= end:
            if tokens[begin] <= power:
                # play the token face up
                power -= tokens[begin]
                score += 1
                begin += 1
                continue
            next = begin + 1
            if next < end and tokens[next] < power + tokens[end] and 0 < score:
                # play the token face down
                power += tokens[end]
                score -= 1
                end -= 1
                continue
            # just ignore
            begin += 1

        return score


class Test(TestCase):
    data: List[Tuple[List[int], int, int]] = [
        # ([100], 50, 0),
        # ([50], 100, 1),
        # ([100, 200], 150, 1),
        ([100, 200, 300, 400], 200, 2),
    ]

    def test_solution(self):
        s = Solution()
        for tokens, power, expected in self.data:
            self.assertEqual(s.bagOfTokensScore(tokens, power), expected)


if __name__ == "__main__":
    main()
