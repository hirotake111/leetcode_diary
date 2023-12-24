/**
 * https://leetcode.com/problems/buy-two-chocolates/
 * 2706. Buy Two Chocolates
 */
impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        let (mut a, mut b) = (101, 101);
        for p in prices {
            if p < a {
                b = a;
                a = p;
            } else if p < b {
                b = p;
            }
        }
        if money >= a + b {
            money - a - b
        } else {
            money
        }
    }
}
