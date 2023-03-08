"""
https://leetcode.com/problems/minimum-time-to-complete-trips/
2187. Minimum Time to Complete Trips
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
"""
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """Binary search approach"""
        # Minimum and maximum of trip times
        min_time = 1
        max_time = time[0] * totalTrips  # This can be any element in time

        while min_time < max_time:
            mid_time = (max_time + min_time) // 2
            # Populate sum of trips
            # (mid_time // t -> the num of trips we can go with the bus within mid_time)
            trips = sum(mid_time // t for t in time)
            if trips >= totalTrips:
                max_time = mid_time
            else:
                min_time = mid_time + 1
        return min_time
