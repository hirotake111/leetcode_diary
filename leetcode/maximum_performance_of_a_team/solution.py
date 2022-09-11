from typing import List, Tuple
from unittest import TestCase, main
import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        """an approach using priority queue"""
        queue: List[int] = []
        answer = total = 0

        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(queue, s)
            total += s

            if len(queue) > k:
                total -= heapq.heappop(queue)

            answer = max(answer, total * e)

        return answer % 1000000007


class Test(TestCase):
    data: List[Tuple[int, List[int], List[int], int, int]] = [
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
        (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
    ]

    def test_solution(self):
        s = Solution()
        for n, speed, efficiency, k, expected in self.data:
            self.assertEqual(s.maxPerformance(n, speed, efficiency, k), expected)


if __name__ == "__main__":
    main()
