"""
https://leetcode.com/problems/break-a-palindrome/
1328. Break a Palindrome
"""
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1 :]
        return palindrome[:-1] + "b" if 2 <= len(palindrome) else ""
