from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        changed = True

        def check(i: int) -> bool:
            pass

        def update(i: int) -> None:
            pass

        while changed:
            for i in range(n - m + 1):
                updatable = check(i)
                if updatable:
                    update(i)
                    changed = True

        return []


class Test(TestCase):
    data: List[Tuple[str, str, List[int]]] = [
        ("abc", "ababc", [0, 2]),
        ("abca", "aabcaca", [3, 0, 1]),
    ]

    def test_solution(self):
        s = Solution()
        for stamp, target, expected in self.data:
            self.assertEqual(s.movesToStamp(stamp, target), expected)


if __name__ == "__main__":
    main()
