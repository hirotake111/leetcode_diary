"""
https://leetcode.com/problems/132-pattern/
456. 132 Pattern
"""
    
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        low_list = list(accumulate(nums, min))
        mid_stack = []

        for i in range(len(nums) -1, -1, -1):
            low = low_list[i]
            high = nums[i]
            if low == high:
                continue

            # Search mid value in mid_list
            while mid_stack and mid_stack[-1] <= low:
                mid_stack.pop()
            
            if mid_stack and mid_stack[-1] < high:
                return True

            # At last, high will be pushed into mid_stack as mid
            mid_stack.append(high)
        
        return False