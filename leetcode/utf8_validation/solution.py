from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx, n = 0, len(data)

        while idx < n:
            if data[idx] < 128:
                idx += 1

            elif 192 <= data[idx] <= 223:
                idx += 1
                if idx < n and 128 <= data[idx] <= 191:
                    idx += 1
                    continue
                return False

            elif 224 <= data[idx] <= 239:
                idx += 1
                for _ in range(2):
                    if idx < n and 128 <= data[idx] <= 191:
                        idx += 1
                        continue
                    return False

            elif 240 <= data[idx] <= 247:
                idx += 1
                for _ in range(3):
                    if 128 <= data[idx] <= 191:
                        idx += 1
                        continue
                    return False

            else:
                return False

        return True


class Test(TestCase):
    data: List[Tuple[List[int], bool]] = [
        ([197, 130, 1], True),
        ([235, 140, 4], False),
        ([237], False),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.validUtf8(input), expected)


if __name__ == "__main__":
    main()
