/**
 * https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
 * 1359. Count All Valid Pickup and Delivery Options
 */

const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn count_orders(n: i32) -> i32 {
        let n = n as i64;
        let total = (1..=(2 * n)).step_by(2).fold(1, |a, c| (a * c) % MOD);
        let factorial = (1..=n).fold(1, |a, c| (a * c) % MOD);
        ((factorial * total) % MOD) as i32
    }
}
