from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        l_to_r, r_to_l = [1] * l, [1] * l

        for i in range(1, l):
            if ratings[i - 1] < ratings[i]:
                l_to_r[i] = l_to_r[i - 1] + 1

        for j in range(l - 2, -1, -1):
            if ratings[j + 1] < ratings[j]:
                r_to_l[j] = r_to_l[j + 1] + 1

        return sum([max(a, b) for a, b in zip(l_to_r, r_to_l)])


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([1, 2, 3], 6),
        ([1, 3, 2, 2, 1], 7),
        ([1, 2, 3, 5, 4, 3, 2, 1], 21),
        ([1, 6, 10, 8, 7, 3, 2], 18),
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 4, 5, 2], 11),
        ([1], 1),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.candy(input), expected)


if __name__ == "__main__":
    main()

"""
[1,0,2]
[1,1,2]
[2,1,2]
[1,3,4,5,4,3,2,3,4,5,6,5,4,5,6,7,8,9,8,7,6,5,6,6,6,6,5,4,3,10]
[1,2,3,4,3,2,1,2,3,4,5,2,1,2,3,4,5,6,4,3,2,1,2,1,1,4,3,2,1,2]
[1,2,3,4,1,2,3,2,3,4,5,1,2,2,3,4,5,6,1,2,3,4,2,1,1,1,2,3,4,2

[4,4,4,5,6]
[1,1,1,2,3]

[1,6,10,8,7,3,2]
[1,2, 5,4,3,2,1]
[1,2, 1,2,3,4,5]

[1,2,3,4,6,9,8,3,2]
[1,2,3,4,5,6,3,2,1]
[1,2,3,4,5,6,1,2,3]

[1,6,7,9,2]
[1,2,3,4,1]

[1,6,7,9,4,3]
[1,2,3,4,2,1]

[1,2,3,5,4,3,2,1]
[1,2,3,4,1,2,3,4]
"""
