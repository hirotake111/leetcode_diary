from unittest import main, TestCase


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def func(start: int, end: int, removed: bool) -> bool:
            ss, se = s[start], s[end]
            if start >= end:
                return True
            if s[start] != s[end]:
                if not removed:
                    # remove one character and resume
                    return func(start + 1, end, True) or func(start, end - 1, True)
                # one character already removed
                return False
            # characters match -> go to next characters
            return func(start + 1, end - 1, removed)

        return func(0, len(s) - 1, False)


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.validPalindrome("aba"), True)
        self.assertEqual(self.s.validPalindrome("abca"), True)
        self.assertEqual(self.s.validPalindrome("abc"), False)
        self.assertEqual(self.s.validPalindrome("abcbaa"), True)
        self.assertEqual(self.s.validPalindrome("abbcbaa"), False)


if __name__ == "__main__":
    main()
