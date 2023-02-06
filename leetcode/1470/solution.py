"""
https://leetcode.com/problems/shuffle-the-array/
1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer: List[int] = [0] * (n * 2)
        for i in range(n):
            answer[i * 2] = nums[i]
            answer[i * 2 + 1] = nums[i + n]
        return answer

        # One liner approach
        # return [ num[i*2+n] if i % 2 else nums[i*2] for i in range(n * 2)]
