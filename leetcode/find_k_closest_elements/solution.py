from logging import setLogRecordFactory
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def is_closer(a: int, b: int):
            return (abs(x - arr[a]) < abs(arr[b] - x)) or (
                abs(arr[a] - x) == abs(arr[b] - x) and arr[a] < arr[b]
            )

        if x <= arr[0]:
            return arr[:k]
        if arr[-1] <= x:
            return arr[-k:]

        low, high = 0, len(arr) - 1
        mid = (low + high) // 2

        while True:
            if arr[mid] == x or mid == low or mid == high:
                # we found mid
                break
            if arr[mid] < x:
                low, mid = mid, (mid + high) // 2
            if x < arr[mid]:
                high, mid = mid, (low + mid) // 2

        low, high = mid - 1, mid + 1
        while high - low + 1 < k:
            if low == 0:
                high += 1
            elif high == len(arr) - 1:
                low -= 1
            elif is_closer(low, high):
                low -= 1
            else:
                high += 1

        return arr[low : high + 1]


class Test(TestCase):
    data: List[Tuple[List[int], int, int, List[int]]] = [
        ([3, 4, 5, 6, 7], 3, 2, [3, 4, 5]),
        ([3, 4, 5, 6, 7], 3, 9, [5, 6, 7]),
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ]

    def test_solution(self):
        s = Solution()
        for arr, k, x, expected in self.data:
            self.assertEqual(s.findClosestElements(arr, k, x), expected)


if __name__ == "__main__":
    main()
