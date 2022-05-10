from unittest import main, TestCase
from typing import Dict, List, Tuple


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans: List[str] = []
        for n in digits:
            if not ans:
                ans = [c for c in d[n]]
                continue
            tmp: List[str] = []
            for current in ans:
                for letter in d[n]:
                    tmp.append(current + letter)
            ans = tmp
        return ans


class TestSolution(TestCase):
    s = Solution()
    data: List[Tuple[str, List[str]]] = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ]

    def test_solution(self):
        for digits, expected in self.data:
            self.assertEqual(self.s.letterCombinations(digits), expected)


if __name__ == "__main__":
    main()
