from unittest import main, TestCase


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        longest = ""

        for i in range(l):
            if i + 1 < l and s[i] == s[i + 1]:  # aa
                for j in range(i + 1):
                    substring = s[i - j : i + j + 2]
                    if i + j + 1 < l and s[i - j] == s[i + j + 1]:
                        if len(longest) < len(substring):
                            longest = substring
                        continue
                    break

            for j in range(i + 1):
                if i + j >= l:
                    break
                substring = s[i - j : i + j + 1]
                if i + j < l and s[i - j] == s[i + j]:
                    if len(longest) < len(substring):
                        longest = substring
                    continue
                break

        return longest


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test_solution(self):
        self.assertIn(self.s.longestPalindrome("babad"), ["bab", "aba"])
        self.assertEqual(self.s.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.s.longestPalindrome("ccc"), "ccc")
        self.assertEqual(self.s.longestPalindrome("accca"), "accca")
        self.assertEqual(self.s.longestPalindrome("aabcdefgh"), "aa")
        self.assertEqual(self.s.longestPalindrome("aaaa"), "aaaa")
        self.assertEqual(
            self.s.longestPalindrome("abbcccbbbcaaccbababcbcabca"), "bbcccbb"
        )


if __name__ == "__main__":
    main()
