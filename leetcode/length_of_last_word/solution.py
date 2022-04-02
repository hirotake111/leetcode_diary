from unittest import main, TestCase


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(self.s.lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(self.s.lengthOfLastWord("luffy is still joyboy"), 6)


if __name__ == "__main__":
    main()
