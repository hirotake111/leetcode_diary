from unittest import main, TestCase


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        n = -1 if x < 0 else 1
        x *= n
        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        result *= n
        if -(2**31) < result < 2**31 - 1:
            return result
        return 0


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.reverse(123), 321)
        self.assertEqual(self.s.reverse(-123), -321)


if __name__ == "__main__":
    main()
