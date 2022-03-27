from unittest import main, TestCase


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n == 0:  # edge case
            return 0
        for i in range(h):
            if haystack[i] != needle[0]:
                continue
            flag = True
            for j in range(n):

                if i + j >= h or haystack[i + j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1


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
