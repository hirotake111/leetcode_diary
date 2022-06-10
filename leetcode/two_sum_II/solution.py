from re import I
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hash map approach
        # d: Dict[int, int] = {}
        # for i, n in enumerate(numbers):
        #     fetched = d.get(target - n)
        #     if fetched is not None:
        #         return [fetched + 1, i + 1]
        #     d[n] = i
        # return []
        i, j = 0, len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            if total < target:
                i += 1
            else:
                j -= 1
        return []


class Test(TestCase):
    def test_solution(self):
        s = Solution()
        data: List[Tuple[List[int], int, List[int]]] = [
            ([1, 2, 3, 4, 7, 10], 10, [3, 5]),
            ([2, 7, 11, 15], 9, [1, 2]),
            ([2, 3, 4], 6, [1, 3]),
            ([-1, 0], -1, [1, 2]),
        ]
        for nums, target, expected in data:
            self.assertEqual(s.twoSum(nums, target), expected)


if __name__ == "__main__":
    main()
