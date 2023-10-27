"""
https://leetcode.com/problems/longest-palindromic-substring/
5. Longest Palindromic Substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = [0, 0]

        def search(l: int, r: int):
            # expand
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1

            l, r = l + 1, r - 1
            if r - l > answer[1] - answer[0]:
                answer[0] = l
                answer[1] = r

        for i in range(len(s)):
            search(i - 1, i + 1)  # aba
            search(i, i + 1)  # aa

        return s[answer[0] : answer[1] + 1]
