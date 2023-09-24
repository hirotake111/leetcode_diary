"""
https://leetcode.com/problems/baseball-game/description/
682. Baseball Game
"""
from unittest import main, TestCase
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans: List[int] = []
        for o in ops:
            if o == "+":
                ans.append(ans[-1] + ans[-2])
            elif o == "D":
                ans.append(ans[-1] * 2)
            elif o == "C":
                ans.pop(-1)
            else:
                ans.append(int(o))

        return sum(ans)


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        ops = ["5", "2", "C", "D", "+"]
        self.assertEqual(self.s.calPoints(ops), 30)
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        self.assertEqual(self.s.calPoints(ops), 27)
        ops = ["1"]
        self.assertEqual(self.s.calPoints(ops), 1)
        ops = ["36", "28", "70", "65", "C", "+", "33", "-46", "84", "C"]
        self.assertEqual(self.s.calPoints(ops), 219)
        ops = [
            "8373",
            "C",
            "9034",
            "-17523",
            "D",
            "1492",
            "7558",
            "-5022",
            "C",
            "C",
            "+",
            "+",
            "-16000",
            "C",
            "+",
            "-18694",
            "C",
            "C",
            "C",
            "-19377",
            "D",
            "-25250",
            "20356",
            "C",
            "-1769",
            "-8303",
            "C",
            "-25332",
            "29884",
            "C",
            "+",
            "C",
            "-29875",
            "-15374",
            "C",
            "+",
            "14584",
            "13773",
            "+",
            "17037",
            "-28248",
            "+",
            "16822",
            "D",
            "+",
            "+",
            "-19357",
            "-26593",
            "-8548",
            "4776",
            "D",
            "-8244",
            "378",
            "+",
            "-19269",
            "-25447",
            "18922",
            "-16782",
            "2886",
            "C",
            "-17788",
            "D",
            "-22256",
            "C",
            "308",
            "-9185",
            "-19074",
            "1528",
            "28424",
            "D",
            "8658",
            "C",
            "7221",
            "-13704",
            "8995",
            "-21650",
            "22567",
            "-29560",
            "D",
            "-9807",
            "25632",
            "6817",
            "28654",
            "D",
            "-18574",
            "C",
            "D",
            "20103",
            "7875",
            "C",
            "9911",
            "23951",
            "C",
            "D",
            "C",
            "+",
            "18219",
            "-20922",
            "D",
            "-24923",
        ]
        self.assertEqual(self.s.calPoints(ops), -16293)


if __name__ == "__main__":
    main()
