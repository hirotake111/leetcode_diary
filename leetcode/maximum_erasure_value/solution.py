from typing import List, Set, Tuple
from unittest import TestCase, main


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        answer, summary = 0, 0
        seen: Set[int] = set()
        while end < len(nums):
            if nums[end] in seen:
                seen.remove(nums[start])
                summary -= nums[start]
                start += 1
            else:
                seen.add(nums[end])
                summary += nums[end]
                answer = max(answer, summary)
                end += 1
        return answer

        # start = 0
        # ans, summary = 0, 0
        # seen: Set = set()
        # for end, n in enumerate(nums):
        #     if n not in seen:
        #         seen.add(n)
        #         summary += n
        #         ans = max(ans, summary)
        #         continue
        #     while start <= end:
        #         if nums[start] == n:
        #             start += 1
        #             break
        #         seen.remove(nums[start])
        #         summary -= nums[start]
        #         start += 1
        # return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8),
        ([4, 2, 4, 5, 6], 17),
        ([10000, 1, 10000, 1, 1, 1, 1, 1, 1], 10001),
        ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.maximumUniqueSubarray(input), expected)


if __name__ == "__main__":
    main()
