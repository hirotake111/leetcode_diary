"""
https://leetcode.com/problems/find-in-mountain-array/
1095. Find in Mountain Array
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, ma: 'MountainArray') -> int:
        memo = [-1] * ma.length()
        l, r = 0, ma.length() - 1
        memo[l], memo[r] = ma.get(l), ma.get(r)

        # Handy function
        def get(i: int) -> int:
            if memo[i] == -1:
                memo[i] = ma.get(i)
            return memo[i]
        
        # shortcut
        if target < min(get(l), get(r)):
            return -1

        def find_peak(l:int, r: int) -> int:
            if l >= r:
                return l
            m = (l + r) // 2
            if get(m - 1) < get(m):
                if get(m) > get(m + 1):
                    # found the peak
                    return m
                # the peak is in the right hand side
                return find_peak(m + 1, r)

            elif get(m - 1) > get(m):
                # peak is in the left hand side
                return find_peak(l, m)

            else:
                # peak is either in the left or right hand side
                left = find_peak(l, m)
                return left if left >= 0 else find_peak(m + 1, r)

        peak = find_peak(l, r)

        if get(peak) < target:
            return -1

        # search the range between 0 to peak
        r = peak
        while l < r:
            m = (l + r) // 2
            if get(m) < target:
                l = m + 1
            else:
                r = m

        if get(l) == target:
            # found the index
            return l

        # search the range between peak to ma.length() - 1
        l, r = peak, ma.length() - 1
        while l < r:
            m = (l + r) // 2
            if get(m) > target:
                l = m + 1
            else:
                r = m

        return l if get(l) == target else -1
