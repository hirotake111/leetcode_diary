"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        nums = 0

        # Populate the number of vowels in the first substring
        sub = s[0:k]
        for c in sub:
            if c in vowels:
                nums += 1

        current = nums
        for i in range(1, len(s) - k + 1):
            # If the right most char is a vowel -> +1
            if s[i + k - 1] in vowels:
                current += 1
            # If the previous left most char is a vowel -> -1
            if s[i - 1] in vowels:
                current -= 1
            nums = max(nums, current)
        return nums
