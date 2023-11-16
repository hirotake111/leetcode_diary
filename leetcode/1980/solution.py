"""
https://leetcode.com/problems/find-unique-binary-string/
1980. Find Unique Binary String
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hs = set([int(s, 2) for s in nums])
        answer = 0
        while answer in hs:
            answer += 1
        bin_str = bin(answer)[2:]
        zeros = "0" * (len(nums) - len(bin_str))
        return f"{zeros}{bin_str}"
