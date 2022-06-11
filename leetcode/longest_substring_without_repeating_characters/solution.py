from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, longest, seen = 0, 0, set()

        for j in range(len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                longest = max(j - i + 1, longest)
                continue

            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    break
                seen.remove(s[i])
                i += 1

        return longest


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, int]] = [
        ("tmmzuxt", 5),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.lengthOfLongestSubstring(input), expected)


if __name__ == "__main__":
    main()
