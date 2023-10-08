/**
 * https://leetcode.com/problems/max-dot-product-of-two-subsequences/
 * 1458. Max Dot Product of Two Subsequences
 */
impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (m, n) = (nums1.len(), nums2.len());
        let mut prev: Vec<i32> = vec![-1001; n + 1];
        let mut answer = -1001;

        for n1 in nums1.iter().rev() {
            let mut dp: Vec<i32> = vec![-1001; n + 1];
            for (i, n2) in nums2.iter().enumerate().rev() {
                let product = n1 * n2 + (0).max(prev[i + 1]);
                dp[i] = product.max(dp[i + 1]).max(prev[i]);
            }
            answer = answer.max(dp[0]);
            prev = dp;
        }

        answer
    }
}
