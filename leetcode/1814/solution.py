"""
https://leetcode.com/problems/count-nice-pairs-in-an-array/
1814. Count Nice Pairs in an Array
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        total = 0
        MOD = 1_000_000_007
        freq = defaultdict(int)

        for n in nums:
            freq[n - int(str(n)[::-1])] += 1

        for v in filter(lambda x: x > 1, freq.values()):
            total = (total + (v * (v - 1) // 2)) % MOD

        return total
