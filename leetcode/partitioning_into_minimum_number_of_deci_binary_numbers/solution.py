from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

        # return max([int(c) for c in n])

        # ans = 0
        # for c in n:
        # ans = max(ans, int(c))
        # return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, int]] = [("32", 3), ("82734", 8), ("27346209830709182346", 9)]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.minPartitions(input), expected)


if __name__ == "__main__":
    main()
