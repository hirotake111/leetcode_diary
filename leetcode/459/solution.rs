/**
 * https://leetcode.com/problems/repeated-substring-pattern/
 * 459. Repeated Substring Pattern
 */

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        for i in 1..s.len() {
            let (quotient, reminder, sub_string) = (s.len() / i, s.len() % i, &s[0..i]);
            if reminder == 0 && sub_string.repeat(quotient) == s {
                return true;
            }
        }
        false
    }
}
