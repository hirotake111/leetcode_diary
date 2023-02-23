"""
https://leetcode.com/problems/ipo/
502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, 
LeetCode would like to work on some projects to increase its capital before the IPO. 
Since it has limited resources, it can only finish at most k distinct projects before the IPO. 
Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
The answer is guaranteed to fit in a 32-bit signed integer.
"""
from typing import List, Tuple
from heapq import heappop, heappush
from unittest import TestCase, main


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted([(c, p) for p, c in zip(profits, capital)])
        # Create a priority queue called availables
        availables: List[int] = []
        i, n = 0, len(profits)
        # Loop as long as i < n, and you still have k
        while i < n and k:
            # Pick up one project (capital, profit)
            ctl, pft = projects[i]
            if ctl <= w:
                # Push it to availables
                heappush(availables, -pft)
                i += 1
            else:
                # cannot finish the project with current w
                # -> pop one available project from the priority queue
                if len(availables) == 0:
                    # no availabble projects -> done
                    break
                # Pick up the largest profit from the priority queue and add it to w
                pft = -heappop(availables)
                w += pft
                k -= 1

        # It's possible that we can finish another k projects
        while k and len(availables):
            # Pick up the largest profit from the priority queue and add it to w
            pft = -heappop(availables)
            w += pft
            k -= 1

        return w


class Test(TestCase):
    cases: List[Tuple[int, int, List[int], List[int], int]] = [
        (2, 0, [1, 2, 3], [0, 1, 1], 4),
    ]

    def test_solution(self):
        for k, w, profits, capital, expected in self.cases:
            solution = Solution()
            self.assertEqual(
                solution.findMaximizedCapital(k, w, profits, capital), expected
            )


if __name__ == "__main__":
    main()
