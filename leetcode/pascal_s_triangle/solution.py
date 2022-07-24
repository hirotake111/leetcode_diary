from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer: List[List[int]] = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return answer

        prev_arr = answer[1]

        for _ in range(numRows - 2):
            new_arr: List[int] = [1]
            for i in range(len(prev_arr) - 1):
                new_arr.append(prev_arr[i] + prev_arr[i + 1])
            new_arr.append(1)
            answer.append(new_arr)
            prev_arr = new_arr

        return answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, List[List[int]]]] = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ]

    def test_solution(self):
        for i, expected in self.data:
            self.assertEqual(self.s.generate(i), expected)


if __name__ == "__main__":
    main()
