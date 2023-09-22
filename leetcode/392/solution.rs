/**
 * https://leetcode.com/problems/is-subsequence/
 * 392. Is Subsequence
 */
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let len_s = s.len();
        let len_t = t.len();

        if len_s == 0 {
            return true;
        }
        if len_s > len_t || len_t == 0 {
            return false;
        }

        let mut i = 0;
        for char_t in t.chars() {
            if s[i] == char_t {
                i += 1;
                if i == len_s {
                    return true;
                }
            }
        }
        false
    }
}
