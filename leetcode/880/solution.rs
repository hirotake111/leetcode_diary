/**
 * https://leetcode.com/problems/decoded-string-at-index/
 * 880. Decoded String at Index
 */

impl Solution {
    pub fn decode_at_index(s: String, k: i32) -> String {
        let mut k = k as u64;
        let mut l: u64 = 0;
        for c in s.chars() {
            l = match c.to_digit(10) {
                Some(n) => l * n as u64,
                None => l + 1,
            }
        }

        for c in s.chars().rev() {
            match c.to_digit(10) {
                Some(n) => {
                    l /= n as u64;
                    k %= l;
                }
                None => {
                    if k == 0 || k == l {
                        return c.to_string();
                    }
                    l -= 1;
                }
            }
        }
        unreachable!()
    }
}
