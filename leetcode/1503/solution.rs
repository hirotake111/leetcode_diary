/**
 * https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
 * 1503. Last Moment Before All Ants Fall Out of a Plank
 */

impl Solution {
    pub fn get_last_moment(n: i32, left: Vec<i32>, right: Vec<i32>) -> i32 {
        match (left.iter().max(), right.iter().min()) {
            (None, None) => 0,
            (None, Some(&r)) => n - r,
            (Some(&l), None) => l,
            (Some(&l), Some(&r)) => l.max(n - r),
        }
    }
}
