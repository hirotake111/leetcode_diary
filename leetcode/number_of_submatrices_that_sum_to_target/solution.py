from collections import Counter
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        answer = 0
        counter: Counter[int] = Counter()
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

        for i in range(n):
            for j in range(i, n):
                counter.clear()
                counter[0] = 1
                current = 0
                for k in range(m):
                    current += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    answer += counter[current - target]
                    counter[current] += 1
        return answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int, int]] = [
        ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4),
        ([[1, -1], [-1, 1]], 0, 5),
        ([[904]], 0, 0),
    ]

    def test_solution(self):
        for matrix, target, expected in self.data:
            self.assertEqual(self.s.numSubmatrixSumTarget(matrix, target), expected)


if __name__ == "__main__":
    main()
