/**
 * https://leetcode.com/problems/frequency-of-the-most-frequent-element/
 * 1838. Frequency of the Most Frequent Element
 */

impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32) -> i32 {
        let mut nums: Vec<i64> = nums.into_iter().map(|n| n as i64).collect();
        nums.sort_unstable();
        let mut answer: i64 = 1;
        let mut total: i64 = nums[0] + k as i64;
        let mut width: i64 = 2;
        let mut l = 0;
        for r in 1..nums.len() {
            total += nums[r];
            // move l
            while total < nums[r] * width {
                total -= nums[l];
                l += 1;
                width -= 1;
            }
            answer = answer.max(width);
            width += 1;
        }

        answer as i32
    }
}
