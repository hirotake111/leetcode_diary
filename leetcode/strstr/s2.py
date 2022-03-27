from unittest import main, TestCase

"""
  |
onionaoneoas
 oneoas
000100
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        self.assertEqual(self.s.strStr(haystack="hello", needle="ll"), 2)
        self.assertEqual(self.s.strStr(haystack="aaaaa", needle="bba"), -1)
        self.assertEqual(self.s.strStr(haystack="", needle=""), 0)
        self.assertEqual(
            self.s.strStr(haystack="asfmkeasmkelfmelwl;opoifm;;;;;", needle="fm"), 2
        )
        self.assertEqual(self.s.strStr(haystack="", needle="a"), -1)


if __name__ == "__main__":
    main()
