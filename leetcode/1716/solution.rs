/**
 * https://leetcode.com/problems/calculate-money-in-leetcode-bank/
 * 1716. Calculate Money in Leetcode Bank
 */
impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let (q, r) = (n / 7, n % 7);
        28 * q + 7 * q * (q - 1) / 2 + r * (r + 1) / 2 + q * r
    }
}
