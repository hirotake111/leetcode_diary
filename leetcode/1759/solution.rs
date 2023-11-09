/**
 * https://leetcode.com/problems/count-number-of-homogenous-substrings/
 * 1759. Count Number of Homogenous Substrings
 */

impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        let mut total = 1;
        let mut count = 1;
        let MOD = 1_000_000_007;

        for n in s.chars().collect::<Vec<char>>().windows(2) {
            count = if n[0] == n[1] { (count + 1) % MOD } else { 1 };
            total = (total + count) % MOD;
        }

        total
    }
}
