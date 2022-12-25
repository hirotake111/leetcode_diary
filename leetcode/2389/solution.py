"""
2389. Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answers = [0] * len(queries)
        nums.sort()

        def search(query_idx: int, low: int, high: int) -> int:
            """
            This binary search function returns an index of nums
            that contains max value in nums which is less than or equal to query
            """
            query = queries[query_idx]
            # If query is greater than or equal to nums[high] we no longer need to search it
            if nums[high] <= query:
                return high
            if nums[low] == query:
                return low

            # At this point nums[low] < query < nums[high]
            # populate mid index
            mid = (high - low) // 2 + low
            if nums[mid] == query:
                return mid
            if low + 1 == high:
                # nums[low] < queries[idx] < nums[high] -> return mid
                return mid

            if query < nums[mid]:
                return search(query_idx, low, mid)
            return search(query_idx, mid, high)

        # convert nums into a list of prefix sum
        tmp = 0
        for i, v in enumerate(nums):
            tmp += v
            nums[i] = tmp

        # binary search maximum value which is less than or equal to queries[i]
        for i in range(len(queries)):
            if queries[i] < nums[0]:
                # no values less than query -> answers[i] should be 0 (do nothing)
                continue
            # answer should be searched index + 1
            answers[i] = search(i, 0, len(nums) - 1) + 1

        return answers


class Test(TestCase):
    data: List[Tuple[List[int], List[int], List[int]]] = [
        ([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]),
        ([2, 3, 4, 5], [1], [0]),
    ]

    def test_solution(self):
        s = Solution()
        for nums, queries, expected in self.data:
            self.assertEqual(s.answerQueries(nums, queries), expected)


if __name__ == "__main__":
    main()
