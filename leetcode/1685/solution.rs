/**
 * https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
 * 1685. Sum of Absolute Differences in a Sorted Array
 */
impl Solution {
    pub fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
        let (mut left, mut right) = (0, nums.iter().sum::<i32>());
        let mut i = -1 * nums.len() as i32;
        nums.into_iter()
            .map(|n| {
                let value = right - left + n * i;
                left += n;
                right -= n;
                i += 2;
                value
            })
            .collect()
    }
}
