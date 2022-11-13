from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda x: x != "", s.strip().split(" ")[::-1]))

        # s = s[::-1]
        # i = 0

        # while i < len(s):
        # # skip spaces from the beginning
        # while i < len(s) and s[i] == " ":
        # continue

        # # move on unstil we see a spce, or at the end of s
        # j = i
        # while j < len(s) and s[j] != " ":
        # j += 1

        # # now s[j] is a space
        # substring = s[i:j][::-1]

        # # replace s[i:j] with substring
        # k = 0
        # while i < j:
        # s[i] = substring[k]
        # k += 1
        # i += 1

        # # now i == j

        # return s


class Test(TestCase):
    data_set: List[Tuple[str, str]] = [
        ("the sky is blue", "blue is sky the"),
        ("a good   example", "example good a"),
    ]

    def test_solution(self):
        s = Solution()
        for given, expected in self.data_set:
            self.assertEqual(s.reverseWords(given), expected)


if __name__ == "__main__":
    main()
