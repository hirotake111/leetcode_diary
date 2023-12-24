/**
 * https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
 * 1561. Maximum Number of Coins You Can Get
 */

impl Solution {
    pub fn max_coins(mut piles: Vec<i32>) -> i32 {
        piles.sort_unstable();
        let t = piles.len() / 3;
        piles.iter().skip(t).step_by(2).sum()
    }
}
