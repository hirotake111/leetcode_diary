/**
 * https://leetcode.com/problems/maximum-score-of-a-good-subarray/
 * 1793. Maximum Score of a Good Subarray
 */

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let (mut i, mut j) = (k, k);
        let (mut max, mut min) = (nums[k], nums[k]);
        let mut n = 1;

        while n < nums.len() {
            if i == 0 {
                j += 1;
                min = min.min(nums[j]);
            } else if j == nums.len() - 1 || nums[i - 1] >= nums[j + 1] {
                i -= 1;
                min = min.min(nums[i]);
            } else {
                j += 1;
                min = min.min(nums[j]);
            }
            n += 1;
            max = max.max(min * n as i32);
        }

        max
    }
}
