# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while True:
            if guess(low) == 0:
                return low
            if guess(high) == 0:
                return high

            mid = (high + low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                low = mid + 1
                high -= 1
            else:
                high = mid - 1
                low += 1
