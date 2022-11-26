from typing import List, Tuple
from unittest import TestCase, main
from bisect import bisect_left
from functools import lru_cache


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # sort jobs by startTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        # also sort start time list
        startTime.sort()
        n = len(jobs)

        @lru_cache()
        def search(i: int) -> int:
            if i == n:
                return 0

            # result of skipping current job
            skip = search(i + 1)

            _, end_time, profit = jobs[i]
            # find the index j -> this should be the next job index
            j = bisect_left(startTime, end_time)
            # result of picking up current job
            adding = search(j) + profit
            return max(skip, adding)

        answer = search(0)
        return answer


class Test(TestCase):
    data_set: List[Tuple[List[int], List[int], List[int], int]] = [
        ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
        ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
        ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
    ]

    def test_solution(self):
        s = Solution()
        for start, end, profit, expected in self.data_set:
            self.assertEqual(s.jobScheduling(start, end, profit), expected)


if __name__ == "__main__":
    main()
