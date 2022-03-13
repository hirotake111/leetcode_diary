from unittest import main, TestCase


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        l, reminder = divmod(len(s), 2)
        if reminder:  # 12321
            s1 = s[:l]
            s2 = s[l + 1 :]
            s2 = s2[::-1]

        else:
            s1 = s[:l]
            s2 = s[l:]
            s2 = s2[::-1]

        if s1 == s2:
            return True
        return False


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.isPalindrome(12321), True)
        self.assertEqual(self.s.isPalindrome(9), True)
        self.assertEqual(self.s.isPalindrome(123321), True)
        self.assertEqual(self.s.isPalindrome(99), True)
        self.assertEqual(self.s.isPalindrome(-99), False)


if __name__ == "__main__":
    main()
