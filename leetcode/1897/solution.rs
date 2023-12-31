/**
 * https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
 * 1897. Redistribute Characters to Make All Strings Equal
 */
impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let mut arr = [0; 26];
        for w in &words {
            for b in w.bytes() {
                arr[(b - 97) as usize] += 1;
            }
        }
        for n in arr {
            if n > 0 && n % words.len() > 0 {
                return false;
            }
        }
        true
    }
}
