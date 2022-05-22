from unittest import TestCase, main
from typing import List, Tuple


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans, l = 0, len(s)

        for i in range(l):
            # find palindrome that is the length of odd
            left, right = i - 1, i + 1
            while 0 <= left and right < l and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

            # find palindrome with even length
            left, right = i, i + 1
            while 0 <= left and right < l and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans + l


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, int]] = [("abc", 3), ("aaa", 6)]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.countSubstrings(input), expected)


if __name__ == "__main__":
    main()
