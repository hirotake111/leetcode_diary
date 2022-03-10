from unittest import main, TestCase


# def debug(s: str, i: int, j: int):
#     print(s[j : i + 1])


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, longest, j = set(), 0, 0

        for i in range(len(s)):
            if s[i] in seen:  # we have seen s[i] before
                while i > j:
                    if s[i] == s[j]:  # matched
                        j += 1
                        break
                    # not matched -> remove character from seen
                    seen.remove(s[j])
                    j += 1

            else:  # we haven't seen s[i] -> add it to seen()
                seen.add(s[i])
                longest = max(i - j + 1, longest)

        return longest


class TestSolution(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("abcd"), 4)
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    main()
