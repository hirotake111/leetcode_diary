/**
 * https://leetcode.com/problems/valid-anagram/
 * 242. Valid Anagram
 */
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut counts: [i16; 26] = [0; 26];
        for b in s.bytes() {
            counts[(b - b'a') as usize] += 1;
        }
        for b in t.bytes() {
            counts[(b - b'a') as usize] -= 1;
        }
        counts.into_iter().all(|v| *v == 0)
    }
}
