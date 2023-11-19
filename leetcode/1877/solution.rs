/**
 * https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
 * 1877. Minimize Maximum Pair Sum in Array
 */
impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let l = nums.len() - 1;
        nums.iter()
            .enumerate()
            .fold(0, |acc, (i, n)| acc.max(n + nums[l - i]))
    }
}
