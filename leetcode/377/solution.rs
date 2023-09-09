/**
 * https://leetcode.com/problems/combination-sum-iv/
 * 377. Combination Sum IV
 */
impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let target = target as usize;
        let mut dp: Vec<i32> = vec![-1; target + 1];

        fn search(nums: &Vec<i32>, target: usize, dp: &mut Vec<i32>) -> i32 {
            if dp[target] >= 0 {
                return dp[target];
            }
            let mut total = 0;
            for v in nums.iter().map(|&n| target as i32 - n) {
                if v == 0 {
                    total += 1;
                } else if v > 0 {
                    total += search(&nums, v as usize, dp);
                }
            }
            dp[target] = total;
            total
        }

        search(&nums, target, &mut dp)
    }
}
