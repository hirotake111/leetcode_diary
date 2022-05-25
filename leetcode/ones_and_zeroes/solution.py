from collections import defaultdict
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ans = 0
        d: Dict[str, Dict[str, int]] = {}
        for s in strs:
            for c in s:
                if d.get(s):
                    d[s][c] += 1
                else:
                    d[s][c] = 0
        print(d)

        def dfs(ss: List[str], a: int, b: int, current_answer: int):
            for i, s in enumerate(ss):
                for c in s:
                    if c == "0":
                        a -= 1
                    if c == "1":
                        b -= 1
                    if a < 0 or b < 0:
                        break
                if a >= 0 and b >= 0:
                    current_answer += 1
                current_answer = max(
                    current_answer, dfs(ss[:i] + ss[i + 1 :], a, b, current_answer)
                )
            return current_answer

        ans = dfs(strs, m, n, 0)
        return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], int, int, int]] = [
        (["10", "0001", "111001", "1", "0"], 5, 3, 4),
        (["10", "0", "1"], 1, 1, 2),
    ]

    def test_solution(self):
        for strs, m, n, expected in self.data:
            self.assertEqual(self.s.findMaxForm(strs, m, n), expected)


if __name__ == "__main__":
    main()
