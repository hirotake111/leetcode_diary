"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        # Populate frequencies of s and p
        arr_s, arr_p = [0] * 26, [0] * 26
        for c in p:
            arr_p[ord(c) - 97] += 1
        for i in range(len(p)):
            c = s[i]
            arr_s[ord(c) - 97] += 1

        answer: List[int] = []
        # Compare the first slice
        if arr_s == arr_p:
            answer.append(0)
        for i in range(len(s) - len(p)):
            # update frequency arr_s
            ch_old = s[i]
            ch_new = s[i + len(p)]
            arr_s[ord(ch_old) - 97] -= 1
            arr_s[ord(ch_new) - 97] += 1
            # Compare updated frequency of s with p's
            if arr_s == arr_p:
                answer.append(i + 1)

        return answer
