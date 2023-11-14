/**
 * https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
 * 1930. Unique Length-3 Palindromic Subsequences
 */
impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        use std::collections::HashSet;
        let chars: HashSet<char> = s.chars().collect();

        let mut total = 0;
        for c in &chars {
            let i = s.find(*c).unwrap();
            let j = s.rfind(*c).unwrap();
            if j - i >= 2 {
                let middles: HashSet<char> = s[(i + 1)..j].chars().collect();
                total += middles.len();
            }
        }

        total as i32
    }
}
