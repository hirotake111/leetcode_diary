/**
 * https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
 * 673. Number of Longest Increasing Subsequence
 *
 * Given an integer array nums, return the number of longest increasing subsequences.
 * Notice that the sequence has to be strictly increasing.
 */

impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        // (length of longest subsequences, and it's count)
        let mut dp = vec![(1, 1); nums.len()];
        let mut longest = std::i32::MIN;

        for i in 0..(nums.len() - 1) {
            for j in (i + 1)..nums.len() {
                if nums[i] < nums[j] {
                    let (prev_longest, prev_count) = dp[i];
                    let (mut length, mut count) = dp[j];
                    if length < prev_longest + 1 {
                        length = prev_longest + 1;
                        count = prev_count;
                    } else if length == prev_longest + 1 {
                        count += prev_count;
                    }
                    dp[j] = (length, count);
                    longest = longest.max(length);
                }
            }
        }
        if longest == std::i32::MIN {
            return nums.len() as i32;
        }

        // Return sum of counts having the longest subsequences
        dp.iter()
            .filter(|&x| x.0 == longest)
            .map(|&x| x.1)
            .sum::<i32>()
    }
}
