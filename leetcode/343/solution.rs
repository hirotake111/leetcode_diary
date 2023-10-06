/**
 * https://leetcode.com/problems/integer-break/
 * 343. Integer Break
 */

impl Solution {
    pub fn integer_break(n: i32) -> i32 {
        match ((n / 3) as u32, n % 3) {
            (0, _) | (1, 0) => n - 1,
            (q, 2) => (3_i32).pow(q) * 2,
            (q, 1) => (3_i32).pow(q - 1) * 4,
            (q, _) => (3_i32).pow(q),
        }
    }
}
