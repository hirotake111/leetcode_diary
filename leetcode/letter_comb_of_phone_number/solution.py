from unittest import main, TestCase
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        result = [""]
        comb = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for d in digits:
            words = comb[d]
            l = len(words)
            result = result * l
            result.sort()
            for i in range(len(result)):
                result[i] = result[i] + words[i % l]

        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.letterCombinations("2"), ["a", "b", "c"])
        self.assertEqual(
            self.s.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(self.s.letterCombinations(""), [])


if __name__ == "__main__":
    main()
