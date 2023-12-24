/**
 * https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
 * 1913. Maximum Product Difference Between Two Pairs
 */
impl Solution {
    pub fn max_product_difference(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        nums.sort_unstable();

        nums[n - 1] * nums[n - 2] - nums[0] * nums[1]
    }
}
