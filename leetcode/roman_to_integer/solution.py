from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def romanToInt(self, s: str) -> int:
        i, answer, n = 0, 0, len(s)
        while i < n:
            a = s[i]
            if i < n - 2:
                b = s[i + 1]
                if a == "C" and b == "M":
                    answer += 900
                    i += 2
                    continue
                if a == "C" and b == "D":
                    answer += 400
                    i += 2
                    continue
                if a == "X" and b == "C":
                    answer += 90
                    i += 2
                    continue
                if a == "X" and b == "L":
                    answer += 40
                    i += 2
                    continue
                if a == "I" and b == "X":
                    answer += 9
                    i += 2
                    continue
                if a == "I" and b == "V":
                    answer += 4
                    i += 2
                    continue
            # else
            if a == "M":
                answer += 1000
            elif a == "D":
                answer += 500
            elif a == "C":
                answer += 100
            elif a == "L":
                answer += 50
            elif a == "X":
                answer += 10
            elif a == "V":
                answer += 5
            else:
                answer += 1
            i += 1

        return answer


class Test(TestCase):
    data: List[Tuple[str, int]] = [
        ("MCMXCIV", 1994),
    ]


if __name__ == "__main__":
    main()
