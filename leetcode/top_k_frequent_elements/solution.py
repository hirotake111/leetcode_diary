from collections import Counter
from timeit import timeit
from unittest import main, TestCase
from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans: List[int] = []
        freq: List[int] = []
        d1: Dict[int, int] = {}
        d2: Dict[int, List[int]] = {}

        d1 = Counter(nums)

        for key, val in d1.items():
            if d2.get(val) is None:
                d2[val] = [key]
                freq.append(val)
            else:
                d2[val] = d2[val] + [key]

        freq.sort()
        tmp = 0
        for key in freq[::-1]:
            if tmp == k:
                break
            ans = ans + d2[key]
            tmp += len(d2[key])
        return sorted(ans)


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2), [1, 2])
        self.assertEqual(self.s.topKFrequent(nums=[1], k=1), [1])
        self.assertEqual(self.s.topKFrequent([-1, -1], 1), [-1])
        self.assertEqual(self.s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2), [-1, 2])


if __name__ == "__main__":
    main()
