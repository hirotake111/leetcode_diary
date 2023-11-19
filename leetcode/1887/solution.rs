/**
 * https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
 * 1887. Reduction Operations to Make the Array Elements Equal
 */
impl Solution {
    pub fn reduction_operations(mut nums: Vec<i32>) -> i32 {
        use std::cmp::Reverse;
        nums.sort_unstable_by_key(|n| Reverse(*n));
        let (mut total, mut prev) = (0, 0);
        for (i, n) in nums.into_iter().enumerate() {
            if n != prev {
                total += i;
                prev = n;
            }
        }
        total as i32
    }
}
