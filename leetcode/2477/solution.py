"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
2477. Minimum Fuel Cost to Report to the Capital
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        fuel = [0]

        # Edge case
        if not roads:
            return 0

        # Populate the length of the graph
        l = max([max(a, b) for a, b in roads]) + 1
        # and create an array visited to track cities we visited
        visited: List[int] = [False] * l

        # Create a graph
        graph: List[List[int]] = [[] for _ in range(l)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i: int) -> int:
            """takes an index of current city, returns total reps"""
            # Each city has one rep
            reps = 1
            # Mark as visited (to prevent circular traverse)
            visited[i] = True
            # Loop over graph[i]
            for j in graph[i]:
                # If we haven't visited city j, then recursively get the total number of reps
                if not visited[j]:
                    reps += dfs(j)

            if i == 0:
                # Since this is a goal, we no longer have to add up fuel
                return 0

            # If 0 < reps // seats, we need another car (fuel)
            fuel[0] += reps // seats + 1 if reps % seats else reps // seats
            # Finally, return the total num of reps
            return reps

        dfs(0)
        return fuel[0]


class Test(TestCase):
    data: List[Tuple[List[List[int]], int, int]] = [
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7),
        ([[0, 1], [0, 2], [0, 3]], 5, 3),
    ]

    def test_solution(self):
        solution = Solution()
        for roads, seats, expected in self.data:
            self.assertEqual(solution.minimumFuelCost(roads, seats), expected)


if __name__ == "__main__":
    main()
