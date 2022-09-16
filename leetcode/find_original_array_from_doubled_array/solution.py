from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n, m = len(changed), len(changed) // 2

        if n & 1:
            return []

        original = [-1] * m
        doubled = original.copy()
        begin = end = 0

        for v in sorted(changed):
            if doubled[begin] == v:
                begin += 1
                if m < begin:
                    return []
                continue

            if m <= end:  # too many original elements
                return []

            original[end] = v
            doubled[end] = v * 2
            end += 1

        return original


class Test(TestCase):
    data: List[Tuple[List[int], List[int]]] = [([1, 3, 4, 2, 6, 8], [1, 3, 4])]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.findOriginalArray(input), expected)


if __name__ == "__main__":
    main()
