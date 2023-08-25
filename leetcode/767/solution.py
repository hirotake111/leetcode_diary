"""
https://leetcode.com/problems/reorganize-string/
767. Reorganize String
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = [0] * 26
        max_idx = 0
        for c in s:
            i = ord(c) - 97
            chars[i] += 1
            if chars[max_idx] < chars[i]:
                max_idx = i

        # Shortcut
        if chars[max_idx] > len(s) // 2 + int(len(s) % 2):
            return ""

        answer = ["" for _ in range(len(s))]
        i = 0
        # Fill in the character with the largest frequency into even indexes
        while True:
            answer[i] = chr(max_idx + 97)
            chars[max_idx] -= 1
            if chars[max_idx] == 0:
                break
            i += 2

        # Fill in the rest of the blank
        j = 1
        for k, count in enumerate(chars):
            if count == 0:
                continue
            # We have the next char "k" to be filled in, but not sure if i is available
            for _ in range(count):
                # Find the next available index i
                while answer[i] != "":
                    i += 2
                    if i >= len(s):
                        i = 0 if i % 2 else 1
                answer[i] = chr(k + 97)

        return "".join(answer)
