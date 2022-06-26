from typing import List, Tuple
from unittest import TestCase, main


"""
[1, 2, 3, 4, 5, 6, 1]
[1, 1, 2, 3, 4, 5, 6]
[6, 1, 1, 2, 3, 4, 5]
[5, 6, 1, 1, 2, 3, 4]
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        arr = cardPoints[l - k :] + cardPoints[:k]
        current = ans = sum(arr[:k])

        if l == k:
            return sum(cardPoints)

        for i in range(k):
            current = current + arr[k + i] - arr[i]
            ans = max(ans, current)
        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int]] = [
        ([1, 2, 3, 4, 5, 6, 1], 3, 12),
        ([2, 2, 2], 2, 4),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
    ]

    def test_solution(self):
        for card_points, k, expected in self.data:
            self.assertEqual(self.s.maxScore(card_points, k), expected)


if __name__ == "__main__":
    main()
